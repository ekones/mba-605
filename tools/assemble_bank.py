import json
import random
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tools.bank_v1 as b1
import tools.bank_v2 as b2
import tools.bank_v3 as b3
import tools.bank_v4 as b4
import tools.bank_v5 as b5
import tools.bank_v6 as b6

versions = [
    (1, b1.v1_questions),
    (2, b2.v2_questions),
    (3, b3.v3_questions),
    (4, b4.v4_questions),
    (5, b5.v5_questions),
    (6, b6.v6_questions),
]

# Patterns for target answer positions (0=A, 1=B, 2=C, 3=D, 4=E)
# Each chapter gets a permutation of [0, 1, 2, 3, 4]
patterns = [
    # v1
    [
        [1, 3, 0, 4, 2], # ch1
        [4, 2, 1, 0, 3], # ch2
        [0, 4, 2, 3, 1], # ch3
        [2, 0, 3, 1, 4], # ch4
        [3, 1, 4, 2, 0], # ch5
    ],
    # v2
    [
        [0, 2, 4, 1, 3], # ch1
        [3, 1, 0, 4, 2], # ch2
        [1, 4, 2, 0, 3], # ch3
        [4, 0, 3, 2, 1], # ch4
        [2, 3, 1, 4, 0], # ch5
    ],
    # v3
    [
        [2, 0, 3, 1, 4], # ch1
        [1, 4, 0, 2, 3], # ch2
        [4, 1, 2, 3, 0], # ch3
        [0, 3, 1, 4, 2], # ch4
        [3, 2, 4, 0, 1], # ch5
    ],
    # v4
    [
        [3, 1, 4, 0, 2], # ch1
        [0, 3, 2, 1, 4], # ch2
        [2, 4, 1, 0, 3], # ch3
        [1, 0, 3, 4, 2], # ch4
        [4, 2, 0, 3, 1], # ch5
    ],
    # v5
    [
        [4, 0, 2, 3, 1], # ch1
        [2, 1, 4, 0, 3], # ch2
        [0, 3, 1, 2, 4], # ch3
        [3, 4, 0, 1, 2], # ch4
        [1, 2, 3, 4, 0], # ch5
    ],
    # v6
    [
        [1, 4, 2, 0, 3], # ch1
        [3, 0, 1, 4, 2], # ch2
        [4, 2, 3, 1, 0], # ch3
        [0, 1, 4, 2, 3], # ch4
        [2, 3, 0, 4, 1], # ch5
    ],
]

letters = ['A', 'B', 'C', 'D', 'E']

for v_idx, (v_num, qlist) in enumerate(versions):
    print(f"\nProcessing v{v_num}...")
    assert len(qlist) == 25, f"Expected 25 questions in v{v_num}, got {len(qlist)}"
    
    # Check chapter distribution
    ch_map = {}
    for q in qlist:
        ch = q['chapter']
        ch_map.setdefault(ch, []).append(q)
    
    for ch in range(1, 6):
        assert len(ch_map[ch]) == 5, f"Chapter {ch} in v{v_num} does not have exactly 5 questions!"
    
    v_pattern = patterns[v_idx]
    
    final_questions = []
    q_counter = 1
    
    rng = random.Random(42 + v_num * 100)
    
    for ch_idx, ch in enumerate(range(1, 6)):
        ch_questions = ch_map[ch]
        target_answers = v_pattern[ch_idx]
        
        for q_in_ch, q in enumerate(ch_questions):
            orig_ans_idx = q['answer']
            correct_text = q['options'][orig_ans_idx]
            distractors = [opt for i, opt in enumerate(q['options']) if i != orig_ans_idx]
            
            # Shuffle distractors reproducibly
            rng.shuffle(distractors)
            
            target_idx = target_answers[q_in_ch]
            
            new_options = distractors[:target_idx] + [correct_text] + distractors[target_idx:]
            assert new_options[target_idx] == correct_text
            assert len(new_options) == 5
            
            q_id = f"v{v_num}-q{q_counter:02d}"
            
            final_q = {
                "id": q_id,
                "chapter": ch,
                "topic": q["topic"],
                "difficulty": q.get("difficulty", "orta"),
                "question": q["question"],
                "options": new_options,
                "answer": target_idx,
                "explanation": q["explanation"],
                "source": q["source"]
            }
            
            # Validate options do not have parens
            for opt in new_options:
                if '(' in opt or ')' in opt:
                    print(f"WARNING: Option contains paren in {q_id}: {opt}")
            
            final_questions.append(final_q)
            q_counter += 1
            
    # Verify answers distribution
    ans_counts = Counter(q['answer'] for q in final_questions)
    print(f"v{v_num} answer distribution:", {letters[k]: v for k, v in sorted(ans_counts.items())})
    for k in range(5):
        assert ans_counts[k] == 5, f"v{v_num} does not have exactly 5 {letters[k]}!"
        
    out_data = {
        "id": f"v{v_num}",
        "version": v_num,
        "title": f"Vize Deneme Seti {v_num}",
        "course": "Örgütsel Davranış",
        "createdAt": "2026-11-22",
        "description": "Bölüm 1–5 ders notlarından üretilmiş 25 çoktan seçmeli vize sorusu (her şık harfinde 5 doğru cevap).",
        "questions": final_questions
    }
    
    out_path = f"docs/data/v{v_num}.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"Saved {out_path} ({len(final_questions)} questions)")

print("\nAll 6 versions successfully assembled!")
