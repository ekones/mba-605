#!/usr/bin/env python3
import json
from pathlib import Path

v8_data = {
    "id": "v8",
    "version": 8,
    "title": "Vize Deneme Seti 8",
    "course": "Örgütsel Davranış",
    "createdAt": "2026-11-23",
    "description": "Robbins ve Judge Örgütsel Davranış Pearson test bankası kaynaklı vize deneme seti (25 çoktan seçmeli soru).",
    "questions": [
        # Bölüm 1: Örgütsel Davranışa Giriş (5 soru: A, B, C, D, E)
        {
            "id": "v8-q01",
            "chapter": 1,
            "topic": "Fayol Yönetim Fonksiyonları: Planlama",
            "difficulty": "kolay",
            "question": "Bir perakende şirketinin genel müdür yardımcısı, şirketin önümüzdeki beş yıllık dönemde pazar payını artırmak amacıyla kurumsal hedefleri tanımlamakta, yeni mağaza açılış stratejilerini belirlemekte ve faaliyetleri koordine edecek kapsamlı planlar hazırlamaktadır. Henri Fayol'un yönetim fonksiyonları sınıflandırmasına göre bu yönetici öncelikli olarak hangi fonksiyonu yerine getirmektedir?",
            "options": [
                "Planlama",
                "Örgütleme",
                "Liderlik",
                "Denetim",
                "Eşgüdüm"
            ],
            "answer": 0,
            "explanation": "Planlama fonksiyonu; örgütsel hedeflerin belirlenmesi, bu hedeflere ulaşmak için genel bir strateji geliştirilmesi ve faaliyetlerin entegrasyonu ile koordinasyonu için kapsamlı planlar hazırlanması sürecidir.",
            "source": "Robbins & Judge Bölüm 1 · Fayol Yönetim Fonksiyonları"
        },
        {
            "id": "v8-q02",
            "chapter": 1,
            "topic": "Mintzberg Kişilerarası Rolleri: Lider Rolü",
            "difficulty": "orta",
            "question": "Üretim departmanı müdürü Arzu Hanım, birimindeki çalışanları şirket hedefleri doğrultusunda motive etmekte, yeni çalışanları işe almakta, eğitmekte ve performans değerlendirmeleri yaparak onların kariyer gelişimlerine rehberlik etmektedir. Henry Mintzberg'in yönetsel rolleri modeline göre Arzu Hanım hangi kişilerarası rolü sergilemektedir?",
            "options": [
                "Temsilci",
                "Lider",
                "İrtibat sağlayıcı",
                "Monitör",
                "Girişimci"
            ],
            "answer": 1,
            "explanation": "Lider rolü; astların işe alınması, eğitilmesi, motive edilmesi, yönlendirilmesi ve performanslarının geliştirilmesini içeren temel kişilerarası yönetsel roldür.",
            "source": "Robbins & Judge Bölüm 1 · Mintzberg Kişilerarası Roller"
        },
        {
            "id": "v8-q03",
            "chapter": 1,
            "topic": "Sistematik Çalışma ve Sezgi",
            "difficulty": "orta",
            "question": "Örgütsel davranış disiplininde insan davranışlarını anlamak ve yönetmek için yalnızca kişisel 'sezgilere' güvenmek yerine sistematik çalışma ve bilimsel kanıtların tercih edilmesinin temel bilimsel gerekçesi aşağıdakilerden hangisidir?",
            "options": [
                "Sezgilerin tüm insanlarda tamamen aynı sonuçları vermesi",
                "İnsan davranışlarının hiçbir kurala veya nedene bağlı olmaksızın gelişmesi",
                "İnsan davranışlarının rastgele olmayıp belirli tutarlılıklar ve öngörülebilir kalıplar barındırması",
                "Yöneticilerin bilimsel verilere dayalı kararlar almaktan kaçınması",
                "Örgütlerde durumsal faktörlerin tamamen ortadan kaldırılabilmesi"
            ],
            "answer": 2,
            "explanation": "Sistematik çalışma yaklaşımı, insan davranışlarının rastgele olmadığını; ilişkileri inceleyerek, neden-sonuç bağları kurarak ve bilimsel kanıtlara dayanarak temel tutarlılıkların öngörülebileceğini savunur.",
            "source": "Robbins & Judge Bölüm 1 · Sistematik Çalışmaya Giriş"
        },
        {
            "id": "v8-q04",
            "chapter": 1,
            "topic": "ÖD Katkı Veren Disiplinler: Sosyal Psikoloji",
            "difficulty": "orta",
            "question": "Hem psikoloji hem de sosyoloji disiplinlerinden kavramları harmanlayarak insanların birbirleri üzerindeki etkilerini, tutum değişimini, iletişim kalıplarını, güven inşasını ve grup içi karar alma süreçlerini inceleyen davranış bilim dalı aşağıdakilerden hangisidir?",
            "options": [
                "Klinik Psikoloji",
                "Antropoloji",
                "Siyaset Bilimi",
                "Sosyal psikoloji",
                "Endüstri Mühendisliği"
            ],
            "answer": 3,
            "explanation": "Sosyal psikoloji; psikoloji ve sosyolojinin kesişiminde yer alarak bireylerin birbirini nasıl etkilediği, tutum değişimi, iletişim ve grup süreçlerini inceleyen disiplindir.",
            "source": "Robbins & Judge Bölüm 1 · Katkıda Bulunan Disiplinler"
        },
        {
            "id": "v8-q05",
            "chapter": 1,
            "topic": "ÖD Modelinde Çıktı Değişkenleri: Geri Çekilme Davranışı",
            "difficulty": "zor",
            "question": "Çalışanların örgütle olan bağlarını zihinsel veya fiziksel olarak kopararak işe geç kalma, devamsızlık yapma veya işten ayrılma şeklinde sergiledikleri eylemler dizisi Robbins ve Judge'ın üç seviyeli örgütsel davranış modelinde hangi çıktı değişkeniyle tanımlanır?",
            "options": [
                "Görev performansı",
                "Örgütsel vatandaşlık",
                "Üretkenlik",
                "Grup uyumu",
                "Geri çekilme davranışı"
            ],
            "answer": 4,
            "explanation": "Geri çekilme davranışı; çalışanların kendilerini örgütten fiziksel ya da psikolojik olarak uzaklaştırmak amacıyla sergiledikleri geç gelme, devamsızlık ve işten ayrılma gibi davranışlar kümesidir.",
            "source": "Robbins & Judge Bölüm 1 · Örgütsel Davranış Modeli Çıktıları"
        },

        # Bölüm 2: Çeşitlilik, Biyografik Özellikler ve Yetenek (5 soru: B, C, D, E, A)
        {
            "id": "v8-q06",
            "chapter": 2,
            "topic": "Ayrımcılık Uygulamaları: Yıldırma / Gözdağı",
            "difficulty": "orta",
            "question": "Bir lojistik merkezinde kıdemli vardiya amiri, ekibe yeni katılan bazı çalışanlara sürekli yüksek sesle bağırmakta, onları haksız yere işten çıkarmakla tehdit etmekte ve çalışma ortamında açık bir düşmanlık ve korku iklimi yaratarak baskı kurmaktadır. Bu durum Robbins ve Judge'ın sınıflandırdığı ayrımcılık türlerinden hangisine doğrudan örnektir?",
            "options": [
                "Ayrımcı politikalar",
                "Yıldırma",
                "Cinsel taciz",
                "Dışlama",
                "Nezaketsizlik"
            ],
            "answer": 1,
            "explanation": "Yıldırma (gözdağı verme / intimidation); çalışanları açık tehditler, zorbalık ve düşmanca davranışlarla sindirmeyi hedefleyen bir ayrımcılık uygulamasıdır.",
            "source": "Robbins & Judge Bölüm 2 · İş Yerinde Ayrımcılık Türleri"
        },
        {
            "id": "v8-q07",
            "chapter": 2,
            "topic": "Biyografik Özellikler: Kıdem ve İş Tatmini",
            "difficulty": "orta",
            "question": "Örgütsel davranış alanında kıdem (çalışanın mevcut iş ve kurumdaki hizmet süresi) ile iş tutumları arasındaki ilişkiyi inceleyen geniş kapsamlı ampirik araştırmalara göre aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Kıdem arttıkça iş tatmini belirgin biçimde düşme eğilimine girer.",
                "Kıdem ile devamsızlık arasında güçlü ve pozitif bir ilişki vardır.",
                "Kıdem arttıkça iş tatmini ve örgütsel bağlılık genellikle artma eğilimi gösterir.",
                "Kıdemin iş performansı üzerinde hiçbir açıklayıcı etkisi bulunmamaktadır.",
                "Kıdemli çalışanlar yeni iş yöntemlerini öğrenmeye tamamen kapalıdır."
            ],
            "answer": 2,
            "explanation": "Kıdem ile iş tatmini ve örgütsel bağlılık arasında pozitif bir ilişki mevcuttur; kıdem arttıkça iş tatmini artma, işten ayrılma ve devamsızlık ise azalma eğilimindedir.",
            "source": "Robbins & Judge Bölüm 2 · Biyografik Özellikler: Kıdem"
        },
        {
            "id": "v8-q08",
            "chapter": 2,
            "topic": "Zihinsel Yetenek: Tümdengelimsel Akıl Yürütme",
            "difficulty": "zor",
            "question": "Bir denetim uzmanı, karmaşık finansal kuralları ve genel muhasebe mevzuatını adım adım uygulayarak şirketin hazırladığı spesifik bir bilanço tablosunda yer alan usulsüzlüğün mantıksal nedenini ortaya çıkarmıştır. Bu uzmanın problem çözümünde kullandığı temel zihinsel yetenek boyutu hangisidir?",
            "options": [
                "Hafıza",
                "Sayısal kavrayış",
                "Algısal hız",
                "Tümdengelimsel akıl yürütme",
                "Tümevarımsal akıl yürütme"
            ],
            "answer": 3,
            "explanation": "Tümdengelimsel akıl yürütme (deductive reasoning); genel bir mantık, ilke veya kuraldan yola çıkarak spesifik bir problemin çözümüne ve sonucuna mantıksal olarak ulaşma yeteneğidir.",
            "source": "Robbins & Judge Bölüm 2 · Zihinsel Yetenek Boyutları"
        },
        {
            "id": "v8-q09",
            "chapter": 2,
            "topic": "Fiziksel Yetenek: Statik Güç",
            "difficulty": "orta",
            "question": "Fiziksel yetenek boyutları göz önüne alındığında; bir çalışanın kas kuvvetini harici ve sabit bir nesneye karşı sürekli, kesintisiz bir baskı uygulayarak kullanabilme kapasitesi aşağıdaki kavramlardan hangisiyle açıklanır?",
            "options": [
                "Dinamik güç",
                "Patlayıcı güç",
                "Gövde gücü",
                "Dinamik esneklik",
                "Statik güç"
            ],
            "answer": 4,
            "explanation": "Statik güç; kas kuvvetini bir nesneye karşı sürekli ve sabit bir dirençle kesintisiz olarak uygulayabilme yeteneğini ifade eder.",
            "source": "Robbins & Judge Bölüm 2 · Fiziksel Yetenek Boyutları"
        },
        {
            "id": "v8-q10",
            "chapter": 2,
            "topic": "Etkili Çeşitlilik Yönetimi Programları",
            "difficulty": "orta",
            "question": "Örgütlerde çeşitlilik yönetimi programlarının kalıcı başarı sağlaması ve çalışanlar arasında tepki ya da kutuplaşma yaratmaması için örgüt yönetiminin benimsemesi gereken en etkili stratejik yaklaşım hangisidir?",
            "options": [
                "Farklılıkları avantaja dönüştürecek kapsayıcı bir iklim yaratarak herkes için adil gelişim fırsatları sunması",
                "Yalnızca belirli demografik gruplara ayrıcalıklı kotalar tahsis etmesi",
                "İşe alım ve terfilerde liyakat yerine sadece yüzeysel çeşitlilik hedeflerini gözetmesi",
                "Eğitim programlarında farklılıkları görmezden gelerek herkesi tek tipleştirmeye çalışması",
                "Çeşitlilik hedeflerini yalnızca insan kaynakları departmanının sorumluluğunda bırakması"
            ],
            "answer": 0,
            "explanation": "Başarılı çeşitlilik yönetimi programları; kapsayıcı bir örgüt iklimi oluşturarak bireysel farklılıkların değer gördüğü ve tüm çalışanlara adil fırsatların sunulduğu bir yapı kurmayı hedefler.",
            "source": "Robbins & Judge Bölüm 2 · Çeşitlilik Yönetimi Stratejileri"
        },

        # Bölüm 3: Tutumlar ve İş Tatmini (5 soru: C, D, E, A, B)
        {
            "id": "v8-q11",
            "chapter": 3,
            "topic": "Bilişsel Çelişkiyi Azaltma Faktörleri",
            "difficulty": "zor",
            "question": "Leon Festinger'ın Bilişsel Çelişki Teorisine göre, bireylerin tutumları ve davranışları arasında hissettikleri uyuşmazlığı azaltmak için harcayacakları çabanın yoğunluğunu belirleyen üç temel unsur arasında aşağıdakilerden hangisi YER ALMAZ?",
            "options": [
                "Çelişkiyi yaratan unsurların birey için taşıdığı önem",
                "Bireyin çelişkili unsurları kontrol edebilme derecesi",
                "Bireyin örgütteki hiyerarşik unvanı ve makamı",
                "Çelişkinin devam etmesi halinde bireyin elde edeceği ödüller",
                "Bireyin durum üzerinde hissettiği özgür irade düzeyi"
            ],
            "answer": 2,
            "explanation": "Festinger'a göre çelişkiyi azaltma arzusu üç faktöre bağlıdır: 1) Unsurların önemi, 2) Bireyin unsurları kontrol edebilme derecesi, 3) Çelişkiye bağlı olarak kazanılan ödüller. Bireyin örgütteki makamı veya unvanı bu temel faktörler arasında yer almaz.",
            "source": "Robbins & Judge Bölüm 3 · Bilişsel Çelişki Teorisi"
        },
        {
            "id": "v8-q12",
            "chapter": 3,
            "topic": "İş Tatminsizliğine Tepkiler: İhmal",
            "difficulty": "orta",
            "question": "Kurumundaki yönetim adaletsizliğinden ve düşük ücretten son derece rahatsız olan Mert Bey, işten ayrılmayı göze alamamakta ancak işe sürekli geç gelmekte, görevlerini savsaklamakta, yüksek hata oranlarına kayıtsız kalmakta ve koşulların daha da kötüleşmesine seyirci kalmaktadır. Mert Bey'in bu davranışı EVLN modelinde hangi tepki türüne örnektir?",
            "options": [
                "Çıkış",
                "Ses",
                "Sadakat",
                "İhmal",
                "Gözden çıkarma"
            ],
            "answer": 3,
            "explanation": "İhmal tepkisi; pasif ve yıkıcı bir tepkidir. Çalışan işten doğrudan ayrılmaz ancak devamsızlık yaparak, geç kalarak, çabayı azaltarak koşulların daha da kötüleşmesine izin verir.",
            "source": "Robbins & Judge Bölüm 3 · Tatminsizliğe Verilen Tepkiler (EVLN)"
        },
        {
            "id": "v8-q13",
            "chapter": 3,
            "topic": "Örgütsel Bağlılık Boyutları: Devamlılık Bağlılığı",
            "difficulty": "orta",
            "question": "Bir telekomünikasyon şirketinde on yıldır çalışan Derya Hanım, mevcut işinden ayrılması durumunda kazanılmış kıdem haklarını ve emeklilik avantajlarını kaybedeceğini, piyasada benzer yan haklara sahip başka bir iş bulmasının çok güç olduğunu düşündüğü için kurumunda kalmaya devam etmektedir. Meyer ve Allen modeline göre Derya Hanım'ın sergilediği bağlılık türü hangisidir?",
            "options": [
                "Duygusal bağlılık",
                "Normatif bağlılık",
                "Ahlaki bağlılık",
                "Sosyal bağlılık",
                "Devamlılık bağlılığı"
            ],
            "answer": 4,
            "explanation": "Devamlılık bağlılığı; çalışanın örgütten ayrılmanın ekonomik maliyetlerini ve fırsat kayıplarını hesaplayarak, mecburiyet hissiyle kurumda kalmasını ifade eden bağlılık boyutudur.",
            "source": "Robbins & Judge Bölüm 3 · Örgütsel Bağlılık Boyutları"
        },
        {
            "id": "v8-q14",
            "chapter": 3,
            "topic": "İş Tatminini Ölçme Yöntemleri Karşılaştırması",
            "difficulty": "orta",
            "question": "İş tatminini ölçmede kullanılan 'tek bir genel derecelendirme' yöntemi ile işin ücret, terfi, yönetim gibi yönlerini ayrı ayrı puanlayıp birleştiren 'bileşenlerin toplamı' yönteminin karşılaştırılması hakkında örgütsel araştırmaların ortaya koyduğu temel sonuç hangisidir?",
            "options": [
                "Tek bir soruyla genel tatmin sormak, bileşenlerin toplanması yöntemi kadar geçerli ve etkilidir.",
                "Bileşenlerin toplanması yöntemi her zaman iki kat daha doğru sonuç verir.",
                "Tek bir genel soru sormak bilimsel açıdan tamamen geçersiz kabul edilir.",
                "İki yöntem arasında hiçbir istatistiksel korelasyon bulunmamaktadır.",
                "Bileşenleri toplamak çalışanların algılarını ölçmekte tamamen yetersizdir."
            ],
            "answer": 0,
            "explanation": "Robbins ve Judge'a göre araştırmalar, 'Her şeyi göz önüne aldığınızda işinizden ne kadar memnunsunuz?' şeklindeki tek genel derecelendirme yönteminin şaşırtıcı biçimde karmaşık bileşen puanlama yöntemi kadar geçerli ve güçlü olduğunu ortaya koymuştur.",
            "source": "Robbins & Judge Bölüm 3 · İş Tatmininin Ölçülmesi"
        },
        {
            "id": "v8-q15",
            "chapter": 3,
            "topic": "Temel Öz Değerlendirme ve İş Tatmini",
            "difficulty": "zor",
            "question": "Bireyin kendi değerine, kapasitesine ve çevresindeki olayları kontrol edebilme yetisine olan temel inancını tanımlayan; yüksek düzeyde olduğunda çalışanların kendilerine daha zorlu hedefler koymasını ve yaptıkları işten daha yüksek tatmin duymasını sağlayan kişilik özelliği hangisidir?",
            "options": [
                "Makyavelizm",
                "Temel öz değerlendirme",
                "Öz denetim",
                "Dışsal denetim odağı",
                "Narsisizm"
            ],
            "answer": 1,
            "explanation": "Temel öz değerlendirme (core self-evaluations); bireylerin kendi yeteneklerine ve değerlerine dair temel inançlarıdır. Yüksek temel öz değerlendirmeye sahip kişiler daha yüksek iş tatmini sergilerler.",
            "source": "Robbins & Judge Bölüm 3 · İş Tatminini Etkileyen Faktörler"
        },

        # Bölüm 4: Duygular ve Duygu Durumları (5 soru: D, E, A, B, C)
        {
            "id": "v8-q16",
            "chapter": 4,
            "topic": "Duygular ve Duygu Durumları Karşılaştırması",
            "difficulty": "orta",
            "question": "Örgütsel davranış yazınında duygular (emotions) ile duygu durumları (moods) arasındaki temel farklar dikkate alındığında aşağıdaki ifadelerden hangisi bilimsel olarak doğrudur?",
            "options": [
                "Duygular günlerce sürerken, duygu durumları yalnızca birkaç saniye içinde sona erer.",
                "Duygu durumları her zaman belirli ve somut bir kişi ya da olaya doğrudan yöneliktir.",
                "Duygular genellikle yüz ifadeleriyle dışa vurulmazken, duygu durumları belirgin mimiklerle sergilenir.",
                "Duygular belirli bir kişi ya da nesneye yöneliktir ve kısa sürerken, duygu durumları net bir nedene bağlı olmaksızın daha uzun sürer.",
                "Duygu durumlarının bilişsel işlevler üzerinde hiçbir etkisi bulunmamaktadır."
            ],
            "answer": 3,
            "explanation": "Duygular somut bir olaya/kişiye yöneltilen yoğun ve kısa süreli tepkilerdir; duygu durumları ise genellikle belirli bir bağlamsal nedene dayanmayan, daha az yoğun ve daha uzun süreli hislerdir.",
            "source": "Robbins & Judge Bölüm 4 · Duygular ve Duygu Durumları Farkı"
        },
        {
            "id": "v8-q17",
            "chapter": 4,
            "topic": "Evrensel Temel Duygular",
            "difficulty": "kolay",
            "question": "Paul Ekman ve çağdaş psikologların dünya çapında kültürlerarası araştırmalarla tanımladığı altı temel evrensel duygu arasında aşağıdakilerden hangisi YER ALMAZ?",
            "options": [
                "Öfke",
                "Korku",
                "Şaşkınlık",
                "İğrenme",
                "Kıskançlık"
            ],
            "answer": 4,
            "explanation": "Altı evrensel temel duygu: öfke, korku, üzüntü, mutluluk, iğrenme ve şaşkınlıktır. Kıskançlık bu evrensel temel duygular arasında yer almayıp karmaşık ikincil bir duygudur.",
            "source": "Robbins & Judge Bölüm 4 · Temel Duygular"
        },
        {
            "id": "v8-q18",
            "chapter": 4,
            "topic": "Pozitiflik Yanlılığı (Positivity Offset)",
            "difficulty": "zor",
            "question": "Bireylerin bulundukları ortamda hiçbir özel olay, olumlu veya olumsuz uyarıcı ya da girdi bulunmadığında dahi genel olarak hafif düzeyde olumlu bir duygu durumunu deneyimleme eğilimine ne ad verilir?",
            "options": [
                "Pozitiflik yanlılığı",
                "Duygusal zekâ",
                "Duygusal emek",
                "Duygusal uyumsuzluk",
                "Duygu bulaşması"
            ],
            "answer": 0,
            "explanation": "Pozitiflik yanlılığı (positivity offset); ortamda özel hiçbir uyarıcı veya girdi yokken insanların çoğunluğunun hafif düzeyde pozitif bir duygu durumunda bulunma eğilimidir.",
            "source": "Robbins & Judge Bölüm 4 · Temel Duygu Durumları"
        },
        {
            "id": "v8-q19",
            "chapter": 4,
            "topic": "Duygusal Emek: Yüzeysel Rol",
            "difficulty": "orta",
            "question": "Bir lüks mağazada satış danışmanı olan Murat Bey, kaba bir müşterinin sözlerine içten içe çok öfkelenmiş olmasına rağmen içsel hislerini hiç değiştirmeden yalnızca ses tonunu sakin tutarak ve gülümseyerek müşteriye hizmet vermiştir. Murat Bey'in gerçek duygularını değiştirmeksizin yalnızca dışa vurulan mimiklerini ve davranışlarını kurumsal beklentiye uydurması duygusal emeğin hangi boyutuna örnektir?",
            "options": [
                "Derin rol",
                "Yüzeysel rol",
                "Duygusal bulaşma",
                "Duygusal tükenme",
                "Bilişsel çelişki"
            ],
            "answer": 1,
            "explanation": "Yüzeysel rol (surface acting); çalışanın gerçekte hissettiği duyguları değiştirmeden sadece dışarıya gösterdiği mimikleri ve sergilediği davranışları kurumsal kurallara göre maskelemesidir.",
            "source": "Robbins & Judge Bölüm 4 · Duygusal Emek Boyutları"
        },
        {
            "id": "v8-q20",
            "chapter": 4,
            "topic": "Duygu Düzenleme: Bilişsel Yeniden Değerlendirme",
            "difficulty": "orta",
            "question": "Yönetim kurulu önünde yapacağı kritik sunum öncesinde şiddetli kaygı ve gerginlik yaşayan bir proje müdürü, bu sunumu bir başarısızlık tehdidi veya sınav olarak görmek yerine, kendi yeteneklerini tepe yönetime kanıtlayabileceği harika bir gelişim fırsatı olarak yeniden düşünmüş ve kaygısını yapıcı bir heyecana dönüştürmüştür. Bu müdürün uyguladığı duygu düzenleme stratejisi hangisidir?",
            "options": [
                "Duyguyu bastırma",
                "Durum seçimi",
                "Bilişsel yeniden değerlendirme",
                "Sosyal paylaşım",
                "Dikkati dağıtma"
            ],
            "answer": 2,
            "explanation": "Bilişsel yeniden değerlendirme (cognitive reappraisal); stresli ya da olumsuz bir duruma yüklenen anlamı zihinsel olarak değiştirerek durumun yarattığı duygusal etkiyi olumluya çevirme tekniğidir.",
            "source": "Robbins & Judge Bölüm 4 · Duygu Düzenleme Teknikleri"
        },

        # Bölüm 5: Kişilik ve Değerler (5 soru: E, A, B, C, D)
        {
            "id": "v8-q21",
            "chapter": 5,
            "topic": "Kişiliğin Belirleyicileri: Kalıtım ve Çevre",
            "difficulty": "orta",
            "question": "Farklı aileler ve çevrelerde büyüyen tek yumurta ikizleri üzerinde yürütülen Minnesota İkiz Araştırması gibi bilimsel çalışmalar, bireyler arasındaki kişilik farklılıklarının kökeni hakkında hangi temel sonuca ulaşmıştır?",
            "options": [
                "Kişiliğin oluşumunda kalıtımın hiçbir payı olmayıp tamamen çevre belirleyicidir.",
                "Kişilik yalnızca yetişkinlik dönemindeki iş deneyimleriyle şekillenir.",
                "Kalıtım zekayı belirlerken kişilik özelliklerini hiçbir şekilde etkilemez.",
                "Kişilik ergenlikten sonra her yıl rastgele biçimde köklü değişime uğrar.",
                "Kişilik farklılıklarının yaklaşık yüzde ellisi genetik faktörler ve kalıtımla açıklanmaktadır."
            ],
            "answer": 4,
            "explanation": "Robbins ve Judge'a göre ikiz araştırmaları, kişilik özelliklerindeki varyasyonun yaklaşık %50'sinin kalıtım (genetik faktörler) tarafından belirlendiğini ortaya koymuştur.",
            "source": "Robbins & Judge Bölüm 5 · Kişiliğin Belirleyicileri"
        },
        {
            "id": "v8-q22",
            "chapter": 5,
            "topic": "MBTI Boyutları: Algısal ve Sezgisel",
            "difficulty": "zor",
            "question": "Myers-Briggs Tip Göstergesinde (MBTI) bireyin dünyadan bilgiyi toplama ve algılama biçimini ifade eden boyutta; rutin, pratik adımlara ve somut detaylara odaklanmak yerine büyük resmi, soyut kavramları ve gelecekteki potansiyel olasılıkları görmeyi tercih eden kişilik boyutu hangisidir?",
            "options": [
                "Sezgisel",
                "Duyusal",
                "Düşünen",
                "Yargılayan",
                "İçe dönük"
            ],
            "answer": 0,
            "explanation": "MBTI'da sezgisel (intuitive - N) bireyler büyük resme, soyut bağlantılara ve gelecekteki olasılıklara odaklanırlar; duyusal (sensing - S) bireyler ise somut detaylara ve gerçeklere odaklanır.",
            "source": "Robbins & Judge Bölüm 5 · MBTI Modeli"
        },
        {
            "id": "v8-q23",
            "chapter": 5,
            "topic": "Büyük Beşli ve İş Performansı: Sorumluluk",
            "difficulty": "orta",
            "question": "Robbins ve Judge'ın aktardığı geniş kapsamlı meta-analiz sonuçlarına göre, meslek grubu ve yapılan işin niteliği ne olursa olsun genel iş performansını en güçlü ve en tutarlı biçimde pozitif öngören Büyük Beşli kişilik boyutu aşağıdakilerden hangisidir?",
            "options": [
                "Dışa dönüklük",
                "Sorumluluk",
                "Uyumluluk",
                "Deneyime açıklık",
                "Duygusal denge"
            ],
            "answer": 1,
            "explanation": "Sorumluluk (conscientiousness) boyutu; planlılık, güvenilirlik, azim ve başarı yönelimi içerdiğinden, tüm meslek kollarında iş performansını en tutarlı öngören kişilik özelliğidir.",
            "source": "Robbins & Judge Bölüm 5 · Büyük Beşli ve İş Performansı"
        },
        {
            "id": "v8-q24",
            "chapter": 5,
            "topic": "Karanlık Üçlü: Makyavelizm",
            "difficulty": "orta",
            "question": "Bir organizasyonda kariyer basamaklarını hızla tırmanan bir yönetici; insanları kendi amaçları için manipüle etmekte tereddüt etmemekte, duygusal mesafesini korumakta ve 'amaca giden her yol meşrudur, sonuçlar araçları haklı çıkarır' anlayışıyla hareket etmektedir. Bu yöneticinin baskın kişilik özelliği Karanlık Üçlü boyutlarından hangisiyle açıklanır?",
            "options": [
                "Narsisizm",
                "Psikopati",
                "Makyavelizm",
                "Dışsal denetim",
                "Düşük öz saygı"
            ],
            "answer": 2,
            "explanation": "Makyavelizm; pragmatik bir yaklaşıma sahip, duygusal mesafeyi koruyan, insanları ustaca manipüle eden ve hedefe ulaşmak için araçları meşru gören kişilik boyutudur.",
            "source": "Robbins & Judge Bölüm 5 · Karanlık Üçlü"
        },
        {
            "id": "v8-q25",
            "chapter": 5,
            "topic": "Rokeach Değer Anketi: Amaçsal Değerler",
            "difficulty": "orta",
            "question": "Milton Rokeach tarafından geliştirilen Değer Anketinde; bir bireyin yaşamı boyunca ulaşmak istediği nihai hedefleri ve arzu edilen nihai varoluş durumlarını (örneğin barış dolu bir dünya, özgürlük, refah, aile güvenliği) tanımlayan değer kümesi hangisidir?",
            "options": [
                "Araçsal değerler",
                "İşlevsel değerler",
                "Operasyonel değerler",
                "Amaçsal değerler",
                "Davranışsal değerler"
            ],
            "answer": 3,
            "explanation": "Rokeach'a göre amaçsal (nihai - terminal) değerler bireyin yaşamı boyunca ulaşmayı arzuladığı nihai hedefleri tanımlar; araçsal (instrumental) değerler ise bu hedeflere ulaşmakta tercih edilen davranış biçimleridir.",
            "source": "Robbins & Judge Bölüm 5 · Rokeach Değer Anketi"
        }
    ]
}

Path("docs/data/v8.json").write_text(json.dumps(v8_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("v8.json başarıyla oluşturuldu.")
