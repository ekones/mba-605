/* Örgütsel Davranış · Vize Soru Çözme Platformu
 * Saf JS — data/manifest.json içindeki sürümleri yükler, data/vN.json dosyalarından soruları okur.
 */
(() => {
  "use strict";

  const LETTERS = ["A", "B", "C", "D", "E", "F"];
  const DIFF_LABEL = { kolay: "Kolay", orta: "Orta", zor: "Zor" };
  const LS = { history: "od-quiz-history", settings: "od-quiz-settings", theme: "od-quiz-theme" };
  const MIXED_ID = "__mixed__";
  const MIXED_SIZE = 25;

  const $ = (id) => document.getElementById(id);
  const el = (tag, cls, text) => {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  };

  const state = {
    manifest: null,
    cache: {},        // versionId -> version json
    session: null,
    timerHandle: null,
    reviewFilter: "all",
  };

  // ---------- yardımcılar ----------
  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  const fmtTime = (sec) => {
    sec = Math.max(0, Math.round(sec));
    const m = Math.floor(sec / 60), s = sec % 60;
    return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  };
  const fmtDate = (iso) => {
    try { return new Date(iso).toLocaleDateString("tr-TR", { day: "numeric", month: "long", year: "numeric" }); }
    catch { return iso; }
  };
  const readLS = (k, d) => { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } };
  const writeLS = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* yok say */ } };
  const chapterName = (n) => (state.manifest?.chapters?.[String(n)]) || `Bölüm ${n}`;

  const show = (view) => {
    ["homeView", "quizView", "resultView"].forEach((v) => $(v).classList.toggle("hidden", v !== view));
    window.scrollTo({ top: 0 });
  };

  // ---------- tema ----------
  const applyTheme = (t) => { document.documentElement.dataset.theme = t; writeLS(LS.theme, t); };
  applyTheme(readLS(LS.theme, matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
  $("themeToggle").addEventListener("click", () =>
    applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark"));

  // ---------- ayarlar ----------
  const settingsEls = { mode: $("modeSelect"), time: $("timeSelect"), shuffleQ: $("shuffleQ"), shuffleO: $("shuffleO") };
  const loadSettings = () => {
    const s = readLS(LS.settings, {});
    if (s.mode) settingsEls.mode.value = s.mode;
    if (s.time !== undefined) settingsEls.time.value = String(s.time);
    settingsEls.shuffleQ.checked = !!s.shuffleQ;
    settingsEls.shuffleO.checked = !!s.shuffleO;
  };
  const getSettings = () => ({
    mode: settingsEls.mode.value,
    time: Number(settingsEls.time.value),
    shuffleQ: settingsEls.shuffleQ.checked,
    shuffleO: settingsEls.shuffleO.checked,
  });
  Object.values(settingsEls).forEach((e) => e.addEventListener("change", () => writeLS(LS.settings, getSettings())));

  // ---------- veri ----------
  async function fetchJSON(path) {
    const res = await fetch(path, { cache: "no-store" });
    if (!res.ok) throw new Error(`${path} yüklenemedi (${res.status})`);
    return res.json();
  }
  async function loadVersion(id) {
    if (state.cache[id]) return state.cache[id];
    if (window.QUIZ_DATA && window.QUIZ_DATA.versions && window.QUIZ_DATA.versions[id]) {
      state.cache[id] = window.QUIZ_DATA.versions[id];
      return state.cache[id];
    }
    const meta = state.manifest.versions.find((v) => v.id === id);
    const data = await fetchJSON(`data/${meta.file}`);
    state.cache[id] = data;
    return data;
  }

  // ---------- ana sayfa ----------
  function renderHome() {
    const list = $("versionList");
    list.innerHTML = "";
    const history = readLS(LS.history, {});
    const versions = state.manifest.versions.slice().reverse(); // en yeni önce

    versions.forEach((v) => list.appendChild(versionCard({
      id: v.id,
      tag: v.id.toUpperCase(),
      title: v.title,
      meta: `${v.questionCount} soru · ${fmtDate(v.createdAt)}`,
      hist: history[v.id],
    })));

    if (state.manifest.versions.length > 1) {
      const total = state.manifest.versions.reduce((s, v) => s + v.questionCount, 0);
      list.appendChild(versionCard({
        id: MIXED_ID,
        tag: "KARIŞIK",
        title: "Karışık deneme",
        meta: `Tüm setlerden (${total} soru) rastgele ${MIXED_SIZE} soru`,
        hist: history[MIXED_ID],
        mixed: true,
      }));
    }
  }

  function versionCard({ id, tag, title, meta, hist, mixed }) {
    const c = el("div", "version-card" + (mixed ? " mixed" : ""));
    c.appendChild(el("span", "v-tag", tag));
    c.appendChild(el("h3", null, title));
    c.appendChild(el("div", "v-meta", meta));
    const sc = el("div", "v-score muted");
    sc.textContent = hist
      ? `En iyi: %${hist.best} · Son: %${hist.last} · ${hist.attempts} deneme`
      : "Henüz çözülmedi";
    c.appendChild(sc);
    const b = el("button", "btn btn-primary", "Başla");
    b.addEventListener("click", () => startVersion(id));
    c.appendChild(b);
    return c;
  }

  // ---------- oturum ----------
  async function startVersion(id) {
    try {
      let questions, title, sub;
      if (id === MIXED_ID) {
        const all = await Promise.all(state.manifest.versions.map((v) => loadVersion(v.id)));
        const pool = all.flatMap((d) => d.questions.map((q) => ({ ...q, _from: d.id })));
        questions = shuffle(pool).slice(0, MIXED_SIZE);
        title = "Karışık deneme";
        sub = `${state.manifest.versions.length} setten rastgele seçildi`;
      } else {
        const d = await loadVersion(id);
        questions = d.questions;
        title = d.title;
        sub = d.description || "";
      }
      startSession({ key: id, title, sub, questions });
    } catch (e) {
      alert(e.message);
    }
  }

  function startSession({ key, title, sub, questions }) {
    const s = getSettings();
    let qs = s.shuffleQ ? shuffle(questions) : questions.slice();
    qs = qs.map((q) => {
      let order = q.options.map((_, i) => i);
      if (s.shuffleO) order = shuffle(order);
      return { ...q, order, correct: order.indexOf(q.answer) };
    });
    state.session = {
      key, title, sub, mode: s.mode, timeLimit: s.time * 60,
      questions: qs,
      answers: new Array(qs.length).fill(null),
      flags: new Set(),
      current: 0,
      startedAt: Date.now(),
      finished: false,
      source: questions,
    };
    $("quizTitle").textContent = title;
    $("quizMeta").textContent = `${qs.length} soru · ${s.mode === "practice" ? "Pratik modu" : "Sınav modu"}`
      + (s.time ? ` · ${s.time} dk` : "");
    startTimer();
    renderPalette();
    renderQuestion();
    show("quizView");
  }

  // ---------- zamanlayıcı ----------
  function startTimer() {
    stopTimer();
    const t = $("timer");
    t.classList.remove("hidden", "low");
    const tick = () => {
      const s = state.session;
      const elapsed = (Date.now() - s.startedAt) / 1000;
      if (s.timeLimit) {
        const left = s.timeLimit - elapsed;
        t.textContent = "⏱ " + fmtTime(left);
        t.classList.toggle("low", left <= 60);
        if (left <= 0) { finish(true); }
      } else {
        t.textContent = "⏱ " + fmtTime(elapsed);
      }
    };
    tick();
    state.timerHandle = setInterval(tick, 1000);
  }
  function stopTimer() {
    clearInterval(state.timerHandle);
    state.timerHandle = null;
  }

  // ---------- soru ekranı ----------
  function renderQuestion() {
    const s = state.session;
    const q = s.questions[s.current];
    const sel = s.answers[s.current];
    const locked = s.mode === "practice" && sel !== null;

    $("qNumber").textContent = `Soru ${s.current + 1} / ${s.questions.length}`;
    $("qChapter").textContent = `Bölüm ${q.chapter} · ${chapterName(q.chapter)}`;
    $("qDifficulty").textContent = DIFF_LABEL[q.difficulty] || q.difficulty;
    $("qText").textContent = q.question;
    $("flagBtn").classList.toggle("on", s.flags.has(s.current));

    const ol = $("qOptions");
    ol.innerHTML = "";
    ol.classList.toggle("locked", locked);
    q.order.forEach((origIdx, displayIdx) => {
      const li = el("li", "option");
      li.appendChild(el("span", "letter", LETTERS[displayIdx]));
      li.appendChild(el("span", "otext", q.options[origIdx]));
      if (sel === displayIdx) li.classList.add("selected");
      if (locked) {
        if (displayIdx === q.correct) li.classList.add("correct");
        else if (displayIdx === sel) li.classList.add("wrong");
        li.classList.remove("selected");
      }
      li.addEventListener("click", () => choose(displayIdx));
      ol.appendChild(li);
    });

    const fb = $("qFeedback");
    if (locked) {
      const ok = sel === q.correct;
      fb.className = "feedback " + (ok ? "ok" : "bad");
      fb.innerHTML = "";
      fb.appendChild(el("b", null, ok ? "✓ Doğru!" : `✗ Yanlış — doğru cevap: ${LETTERS[q.correct]}`));
      fb.appendChild(el("div", null, q.explanation));
      if (q.source) fb.appendChild(el("div", "src", "Kaynak: " + q.source));
    } else {
      fb.className = "feedback hidden";
    }

    $("prevBtn").disabled = s.current === 0;
    const last = s.current === s.questions.length - 1;
    $("nextBtn").textContent = last ? "Bitir ✓" : "Sonraki →";

    const answered = s.answers.filter((a) => a !== null).length;
    $("progressBar").style.width = `${(answered / s.questions.length) * 100}%`;
    updatePalette();
  }

  function choose(displayIdx) {
    const s = state.session;
    if (s.finished) return;
    if (s.mode === "practice" && s.answers[s.current] !== null) return;
    // sınav modunda aynı şıkka tekrar tıklamak cevabı temizler
    s.answers[s.current] = (s.mode === "exam" && s.answers[s.current] === displayIdx) ? null : displayIdx;
    renderQuestion();
  }

  function go(i) {
    const s = state.session;
    if (i < 0 || i >= s.questions.length) return;
    s.current = i;
    renderQuestion();
  }

  function renderPalette() {
    const p = $("palette");
    p.innerHTML = "";
    state.session.questions.forEach((_, i) => {
      const b = el("button", null, String(i + 1));
      b.addEventListener("click", () => go(i));
      p.appendChild(b);
    });
  }
  function updatePalette() {
    const s = state.session;
    [...$("palette").children].forEach((b, i) => {
      const a = s.answers[i];
      b.className = "";
      if (a !== null) {
        if (s.mode === "practice") b.classList.add(a === s.questions[i].correct ? "correct" : "wrong");
        else b.classList.add("answered");
      }
      if (s.flags.has(i)) b.classList.add("flagged");
      if (i === s.current) b.classList.add("current");
    });
  }

  function toggleFlag() {
    const s = state.session;
    s.flags.has(s.current) ? s.flags.delete(s.current) : s.flags.add(s.current);
    renderQuestion();
  }

  // ---------- bitirme & sonuç ----------
  function finish(timeUp = false) {
    const s = state.session;
    if (!s || s.finished) return;
    if (!timeUp) {
      const blank = s.answers.filter((a) => a === null).length;
      const msg = blank
        ? `${blank} soru boş. Yine de bitirmek istiyor musun?`
        : "Sınavı bitirmek istiyor musun?";
      if (!confirm(msg)) return;
    }
    s.finished = true;
    s.duration = (Date.now() - s.startedAt) / 1000;
    stopTimer();
    $("timer").classList.add("hidden");
    if (timeUp) alert("Süre doldu! Sonuçlar gösteriliyor.");
    renderResults();
    show("resultView");
  }

  function renderResults() {
    const s = state.session;
    let correct = 0, wrong = 0, blank = 0;
    const byCh = {};
    s.questions.forEach((q, i) => {
      const a = s.answers[i];
      const c = (byCh[q.chapter] ||= { total: 0, ok: 0 });
      c.total++;
      if (a === null) blank++;
      else if (a === q.correct) { correct++; c.ok++; }
      else wrong++;
    });
    const pct = Math.round((correct / s.questions.length) * 100);

    // geçmiş (yalnızca tam set denemeleri)
    if (!s.isRetry) {
      const h = readLS(LS.history, {});
      const prev = h[s.key] || { attempts: 0, best: 0 };
      h[s.key] = { attempts: prev.attempts + 1, best: Math.max(prev.best, pct), last: pct, lastDate: new Date().toISOString() };
      writeLS(LS.history, h);
    }

    const ring = $("scoreRing");
    ring.style.setProperty("--pct", pct);
    ring.style.setProperty("--ring-color", pct >= 70 ? "var(--ok)" : pct >= 50 ? "var(--warn)" : "var(--bad)");
    $("scorePct").textContent = `%${pct}`;
    $("resultTitle").textContent =
      (pct >= 85 ? "Harika! " : pct >= 70 ? "Çok iyi! " : pct >= 50 ? "Fena değil. " : "Biraz daha tekrar lazım. ")
      + `${s.title}${s.isRetry ? " (tekrar)" : ""}`;
    $("statCorrect").textContent = correct;
    $("statWrong").textContent = wrong;
    $("statBlank").textContent = blank;
    $("statTime").textContent = fmtTime(s.duration);
    $("retryWrongBtn").disabled = wrong + blank === 0;

    const bd = $("chapterBreakdown");
    bd.innerHTML = "";
    Object.keys(byCh).map(Number).sort((a, b) => a - b).forEach((ch) => {
      const { total, ok } = byCh[ch];
      const row = el("div", "ch-row");
      row.appendChild(el("div", null, `B${ch} · ${chapterName(ch)}`));
      const bar = el("div", "ch-bar");
      const fill = el("div");
      fill.style.width = `${(ok / total) * 100}%`;
      bar.appendChild(fill);
      row.appendChild(bar);
      row.appendChild(el("div", "ch-val", `${ok}/${total}`));
      bd.appendChild(row);
    });

    state.reviewFilter = "all";
    [...$("reviewFilter").children].forEach((b) => b.classList.toggle("active", b.dataset.filter === "all"));
    renderReview();
  }

  function renderReview() {
    const s = state.session;
    const list = $("reviewList");
    list.innerHTML = "";
    s.questions.forEach((q, i) => {
      const a = s.answers[i];
      const status = a === null ? "blank" : a === q.correct ? "correct" : "wrong";
      if (state.reviewFilter !== "all" && state.reviewFilter !== status) return;

      const item = el("div", `review-item ${status}`);
      const head = el("div", "ri-head");
      head.appendChild(el("b", null, `Soru ${i + 1}`));
      head.appendChild(el("span", "badge", `B${q.chapter}`));
      head.appendChild(el("span", "badge badge-soft", q.topic));
      head.appendChild(el("span", "muted",
        status === "correct" ? "✓ Doğru" : status === "wrong" ? `✗ Senin cevabın: ${LETTERS[a]}` : "— Boş"));
      item.appendChild(head);
      item.appendChild(el("p", "ri-q", q.question));
      const ul = el("ul");
      q.order.forEach((orig, d) => {
        const li = el("li", null, `${LETTERS[d]}) ${q.options[orig]}`);
        if (d === q.correct) li.classList.add("is-correct");
        else if (d === a) li.classList.add("is-wrong");
        ul.appendChild(li);
      });
      item.appendChild(ul);
      item.appendChild(el("p", "ri-exp", q.explanation + (q.source ? `  (Kaynak: ${q.source})` : "")));
      list.appendChild(item);
    });
    if (!list.children.length) list.appendChild(el("p", "muted", "Bu filtrede soru yok."));
  }

  $("reviewFilter").addEventListener("click", (e) => {
    const f = e.target.dataset?.filter;
    if (!f) return;
    state.reviewFilter = f;
    [...$("reviewFilter").children].forEach((b) => b.classList.toggle("active", b === e.target));
    renderReview();
  });

  $("retryWrongBtn").addEventListener("click", () => {
    const s = state.session;
    const subset = s.questions
      .filter((q, i) => s.answers[i] !== q.correct)
      .map(({ order, correct, ...orig }) => orig);
    if (!subset.length) return;
    startSession({ key: s.key, title: s.title, sub: s.sub, questions: subset });
    state.session.isRetry = true;
    $("quizMeta").textContent = `${subset.length} soru · yanlış & boşların tekrarı`;
  });
  $("retryAllBtn").addEventListener("click", () => {
    const s = state.session;
    if (s.key === MIXED_ID) startVersion(MIXED_ID);
    else startVersion(s.key);
  });
  $("backHomeBtn").addEventListener("click", goHome);

  function goHome() {
    const s = state.session;
    if (s && !s.finished && s.answers.some((a) => a !== null)) {
      if (!confirm("Devam eden sınavdan çıkılsın mı? İlerlemen kaybolacak.")) return;
    }
    stopTimer();
    $("timer").classList.add("hidden");
    state.session = null;
    renderHome();
    show("homeView");
  }

  // ---------- olaylar ----------
  $("homeLink").addEventListener("click", (e) => { e.preventDefault(); goHome(); });
  $("prevBtn").addEventListener("click", () => go(state.session.current - 1));
  $("nextBtn").addEventListener("click", () => {
    const s = state.session;
    if (s.current === s.questions.length - 1) finish();
    else go(s.current + 1);
  });
  $("finishBtn").addEventListener("click", () => finish());
  $("flagBtn").addEventListener("click", toggleFlag);

  document.addEventListener("keydown", (e) => {
    const s = state.session;
    if (!s || s.finished || $("quizView").classList.contains("hidden")) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement?.tagName)) return;
    const k = e.key.toLowerCase();
    const n = s.questions[s.current].options.length;
    let idx = "abcde".indexOf(k);
    if (idx === -1 && /^[1-5]$/.test(k)) idx = Number(k) - 1;
    if (idx >= 0 && idx < n) { choose(idx); e.preventDefault(); return; }
    if (k === "arrowright" || k === "enter") { $("nextBtn").click(); e.preventDefault(); }
    else if (k === "arrowleft") { go(s.current - 1); e.preventDefault(); }
    else if (k === "f") { toggleFlag(); e.preventDefault(); }
  });

  window.addEventListener("beforeunload", (e) => {
    const s = state.session;
    if (s && !s.finished && s.answers.some((a) => a !== null)) { e.preventDefault(); e.returnValue = ""; }
  });

  // ---------- başlat ----------
  loadSettings();
  if (window.QUIZ_DATA && window.QUIZ_DATA.manifest) {
    state.manifest = window.QUIZ_DATA.manifest;
    renderHome();
  } else {
    fetchJSON("data/manifest.json")
      .then((m) => { state.manifest = m; renderHome(); })
      .catch((err) => {
        const box = $("loadError");
        box.classList.remove("hidden");
        box.innerHTML = "";
        box.appendChild(el("div", null, "Soru verileri yüklenemedi: " + err.message));
        box.appendChild(el("div", "small",
          "Dosyayı doğrudan açmak yerine bir yerel sunucu üzerinden aç: python3 -m http.server 8000 --directory docs"));
      });
  }
})();
