#!/usr/bin/env python3
import json
from pathlib import Path

v10_data = {
    "id": "v10",
    "version": 10,
    "title": "Vize Deneme Seti 10",
    "course": "Örgütsel Davranış",
    "createdAt": "2026-11-23",
    "description": "Robbins ve Judge Örgütsel Davranış Pearson test bankası kaynaklı vize deneme seti (25 çoktan seçmeli soru).",
    "questions": [
        # Bölüm 1: Örgütsel Davranışa Giriş (B, D, A, E, C)
        {
            "id": "v10-q01",
            "chapter": 1,
            "topic": "Mintzberg Karar Alma Rolleri: Girişimci Rolü",
            "difficulty": "orta",
            "question": "Bir perakende şirketinin tepe yöneticisi pazardaki değişen tüketici eğilimlerini inceleyerek şirket içinde yapay zekâ tabanlı yeni bir e-ticaret lojistik projesi başlatmış, bu projenin kaynaklarını bizzat tahsis etmiş ve değişimi yönlendirmiştir. Henry Mintzberg'in yönetsel rolleri modelinde organizasyon içinde kontrollü değişimi ve yenilikçi projeleri başlatan rol hangisidir?",
            "options": [
                "Sorun çözücü",
                "Girişimci",
                "Kaynak dağıtıcı",
                "Müzakereci",
                "Monitör"
            ],
            "answer": 1,
            "explanation": "Girişimci rolü; yöneticinin örgüt içinde yeni fırsatları araması, yenilikçi projeleri başlatması ve kontrollü kurumsal değişimi tasarlayıp yürütmesini içeren karar alma rolüdür.",
            "source": "Robbins & Judge Bölüm 1 · Mintzberg Karar Alma Rolleri"
        },
        {
            "id": "v10-q02",
            "chapter": 1,
            "topic": "Örgütsel Etkinlik ve Verimlilik Farkı",
            "difficulty": "orta",
            "question": "Bir beyaz eşya fabrikası belirlenen 50.000 adetlik ihracat siparişi hedefine müşterinin istediği tarihte eksiksiz ulaşmıştır; ancak üretim sürecinde bütçelenenin yüzde kırk üzerinde hammadde israf edilmiş ve aşırı mesai ücreti ödenmiştir. Bu fabrikanın örgütsel performans kriterleri açısından değerlendirmesi aşağıdakilerden hangisinde en doğru yapılmıştır?",
            "options": [
                "Fabrika hem etkin hem de verimli çalışmıştır.",
                "Fabrika verimli çalışmış fakat etkinliğe ulaşamamıştır.",
                "Fabrika ne etkin ne de verimli olabilmiştir.",
                "Fabrika etkinliğe ulaşmış fakat verimliliği düşük kalmıştır.",
                "Fabrikada yalnızca örgütsel vatandaşlık davranışı yükselmiştir."
            ],
            "answer": 3,
            "explanation": "Etkinlik belirlenen hedeflere ulaşma derecesidir (sipariş tamamlanmıştır). Verimlilik ise hedefe ulaşırken kaynakların ne ölçüde tasarruflu kullanıldığıdır (aşırı kaynak tüketildiği için verimlilik düşüktür).",
            "source": "Robbins & Judge Bölüm 1 · Örgütsel Performans: Etkinlik ve Verimlilik"
        },
        {
            "id": "v10-q03",
            "chapter": 1,
            "topic": "Durumsallık Yaklaşımı (Contingency Variables)",
            "difficulty": "kolay",
            "question": "Örgütsel davranış biliminde insan davranışlarının karmaşık yapısı gereği herkes için her koşulda geçerli olan evrensel ve mutlak kurallar yerine, 'X eylemi Y sonucunu doğurur; ancak yalnızca Z şartı altında' şeklinde koşullara bağlı açıklamalar getiren temel kavram aşağıdakilerden hangisidir?",
            "options": [
                "Durumsallık değişkenleri",
                "Bağımsız değişkenler",
                "Çıktı değişkenleri",
                "Genel geçer kurallar",
                "Sezgisel yaklaşımlar"
            ],
            "answer": 0,
            "explanation": "Durumsallık yaklaşımı (contingency approach); örgütsel davranışta basit ve evrensel ilkelerin bulunmadığını, neden-sonuç ilişkilerinin durumsal faktörler (koşullar) tarafından biçimlendiğini savunur.",
            "source": "Robbins & Judge Bölüm 1 · Durumsallık Değişkenleri"
        },
        {
            "id": "v10-q04",
            "chapter": 1,
            "topic": "Fred Luthans Araştırması: Başarılı Yöneticiler",
            "difficulty": "zor",
            "question": "Fred Luthans ve ekibinin yöneticiler üzerinde yaptığı ampirik araştırmalara göre; kurum içinde en hızlı terfi eden 'başarılı' yöneticilerin zamanlarının en büyük payını ayırdıkları yönetsel faaliyet aşağıdakilerden hangisidir?",
            "options": [
                "Geleneksel yönetim ve planlama",
                "Teknik analiz ve bütçeleme",
                "İnsan kaynakları yönetimi ve eğitim",
                "Rutin bilgi alışverişi ve yazışma",
                "Sosyal ağ kurma ve politik ilişkiler"
            ],
            "answer": 4,
            "explanation": "Luthans'ın araştırmasında kurum içinde en hızlı terfi eden 'başarılı' yöneticilerin zamanlarının yaklaşık %48'ini sosyal ağ kurmaya (networking - kurum içi ve dışı ilişkiler) ayırdıkları tespit edilmiştir.",
            "source": "Robbins & Judge Bölüm 1 · Başarılı ve Etkili Yöneticiler"
        },
        {
            "id": "v10-q05",
            "chapter": 1,
            "topic": "ÖD Modelinde Örgüt Sistemi Düzeyi Süreçler",
            "difficulty": "orta",
            "question": "Robbins ve Judge'ın üç seviyeli örgütsel davranış modelinde (birey, grup, örgüt sistemi); en üst düzey olan 'Örgüt Sistemi' düzeyinde analiz edilen 'Süreç' değişkenleri arasında hangisi yer alır?",
            "options": [
                "Bireysel algı ve karar verme",
                "Grup içi çatışma dinamikleri",
                "İnsan kaynakları yönetimi uygulamaları ve değişim süreçleri",
                "Çalışanın iş tatmini ve stresi",
                "Takım üyelerinin kişilik özellikleri"
            ],
            "answer": 2,
            "explanation": "Modelde örgüt sistemi düzeyindeki süreçler insan kaynakları politikaları, kurumsal uygulamalar ve örgütsel değişim uygulamalarıdır.",
            "source": "Robbins & Judge Bölüm 1 · ÖD Analiz Düzeyleri"
        },

        # Bölüm 2: Çeşitlilik, Biyografik Özellikler ve Yetenek (D, A, E, C, B)
        {
            "id": "v10-q06",
            "chapter": 2,
            "topic": "Ayrımcılık Uygulamaları: Dışlama",
            "difficulty": "orta",
            "question": "Bir yatırım şirketinde tepe yönetici kadrosunun şirket dışındaki önemli müşteri yemeklerine, golf kulübü buluşmalarına ve gayriresmi terfi görüşmelerine kadın yöneticileri ve belirli etnik kökenden gelen çalışanları kasıtlı olarak davet etmemesi Robbins ve Judge tarafından hangi ayrımcılık türüyle tanımlanır?",
            "options": [
                "Yıldırma",
                "Cinsel taciz",
                "Nezaketsizlik",
                "Dışlama",
                "Alay ve hakaret"
            ],
            "answer": 3,
            "explanation": "Dışlama (exclusion); belirli bireylerin iş olanaklarından, sosyal etkinliklerden, önemli tartışmalardan ve gayriresmi ağlardan kasıtlı olarak soyutlanmasıdır.",
            "source": "Robbins & Judge Bölüm 2 · İş Yerinde Ayrımcılık Türleri"
        },
        {
            "id": "v10-q07",
            "chapter": 2,
            "topic": "Zihinsel Yetenek: Mekânsal Görselleştirme",
            "difficulty": "zor",
            "question": "Mimarlar, iç mimarlar ve makine tasarımcıları için kritik önem taşıyan; iki veya üç boyutlu bir nesnenin uzaydaki konumu ya da açısı değiştirildiğinde nasıl görüneceğini zihinde canlandırabilme ve tasavvur edebilme yetisi hangi zihinsel yetenek boyutudur?",
            "options": [
                "Mekânsal görselleştirme",
                "Tümevarımsal akıl yürütme",
                "Algısal hız",
                "Sayısal kavrayış",
                "Sözel anlama"
            ],
            "answer": 0,
            "explanation": "Mekânsal görselleştirme (spatial visualization); bir nesnenin uzayda hareket ettirildiğinde veya döndürüldüğünde alacağı konumu ve biçimi zihinde canlandırabilme yeteneğidir.",
            "source": "Robbins & Judge Bölüm 2 · Zihinsel Yetenek Boyutları"
        },
        {
            "id": "v10-q08",
            "chapter": 2,
            "topic": "Derinlemesine Çeşitlilik ve Grup Süreçleri",
            "difficulty": "orta",
            "question": "Yeni kurulan bir proje takımında zaman ilerledikçe ve çalışanlar birbirleriyle daha uzun süre etkileşimde bulunup birbirlerini yakından tanıdıkça, yüzeysel çeşitlilik unsurlarının etkisi azalırken aşağıdaki çeşitlilik unsurlarından hangisinin takım uyumu üzerindeki belirleyiciliği artar?",
            "options": [
                "Yaş farklılıkları",
                "Cinsiyet dağılımı",
                "Fiziksel yetenekler",
                "Etnik köken",
                "Derinlemesine çeşitlilik unsurları"
            ],
            "answer": 4,
            "explanation": "Zaman geçtikçe demografik (yüzeysel) özelliklerin çalışan algıları üzerindeki etkisi azalır; bireylerin değerleri, inançları ve kişilikleri (derinlemesine çeşitlilik) grup dinamiklerinde belirleyici hale gelir.",
            "source": "Robbins & Judge Bölüm 2 · Yüzeysel ve Derinlemesine Çeşitlilik"
        },
        {
            "id": "v10-q09",
            "chapter": 2,
            "topic": "Biyografik Özellikler: Cinsiyet ve Zihinsel Beceriler",
            "difficulty": "orta",
            "question": "Örgütsel davranış alanında kadın ve erkek çalışanların iş yerindeki yetkinlikleri üzerine yapılan binlerce bağımsız araştırmanın meta-analiz sonuçlarına göre aşağıdaki ifadelerden hangisi bilimsel olarak kanıtlanmıştır?",
            "options": [
                "Erkekler karmaşık analitik problemlerde kadınlardan belirgin biçimde daha başarılıdır.",
                "Kadınlar liderlik motivasyonu açısından erkeklerden sürekli daha geridedir.",
                "Kadın ve erkek çalışanlar arasında problem çözme yeteneği, analitik beceri ve iş motivasyonu açısından tutarlı ve anlamlı hiçbir fark yoktur.",
                "Erkek çalışanların örgütsel bağlılığı kadın çalışanlardan her zaman daha yüksektir.",
                "Kadınların öğrenme kabiliyeti teknoloji sektöründe erkeklerden daha düşüktür."
            ],
            "answer": 2,
            "explanation": "Geniş araştırmalar kadınlar ve erkekler arasında zihinsel yetenek, problem çözme, analitik düşünme veya iş motivasyonu bakımından hiçbir anlamlı performans farkı olmadığını göstermektedir.",
            "source": "Robbins & Judge Bölüm 2 · Biyografik Özellikler: Cinsiyet"
        },
        {
            "id": "v10-q09b",
            "chapter": 2,
            "topic": "Fiziksel Yetenek: Patlayıcı Güç",
            "difficulty": "kolay",
            "question": "Bir depo veya inşaat alanında çalışanın bir defalık ya da anlık bir hamlede maksimum kas kuvvetini ve enerjisini aniden açığa çıkarma kabiliyeti hangi fiziksel yetenek boyutuyla tanımlanır?",
            "options": [
                "Statik güç",
                "Patlayıcı güç",
                "Gövde gücü",
                "Dayanıklılık",
                "Denge"
            ],
            "answer": 1,
            "explanation": "Patlayıcı güç (explosive strength); kas gücünü bir kerede veya tek bir patlayıcı hamlede maksimum düzeyde açığa çıkarabilme yeteneğidir.",
            "source": "Robbins & Judge Bölüm 2 · Fiziksel Yetenek Boyutları"
        },

        # Bölüm 3: Tutumlar ve İş Tatmini (A, C, B, D, E)
        {
            "id": "v10-q11",
            "chapter": 3,
            "topic": "Meyer ve Allen: Duygusal Bağlılık",
            "difficulty": "kolay",
            "question": "Çalıştığı şirketin kurumsal misyonunu ve değerlerini gönülden benimseyen, kurumuna karşı güçlü bir aidiyet ve sevgi hisseden ve işinde 'mecbur olduğu için değil, gerçekten kalmak istediği için' çalışan bir uzmanın bağlılığı Meyer ve Allen modeline göre hangi bağlılık türüdür?",
            "options": [
                "Duygusal bağlılık",
                "Devamlılık bağlılığı",
                "Normatif bağlılık",
                "Çıkarcı bağlılık",
                "Mecburi bağlılık"
            ],
            "answer": 0,
            "explanation": "Duygusal bağlılık (affective commitment); çalışanın örgütüyle duygusal bir bağ kurması, onun amaçlarıyla özdeşleşmesi ve kurumda gönüllü olarak kalmak istemesidir.",
            "source": "Robbins & Judge Bölüm 3 · Örgütsel Bağlılık Boyutları"
        },
        {
            "id": "v10-q12",
            "chapter": 3,
            "topic": "Tutumun Duygusal Bileşeni",
            "difficulty": "orta",
            "question": "'Departmanımıza yeni atanan bölge müdüründen hiç hoşlanmıyorum ve onunla aynı toplantıda bulunmak beni son derece öfkelendiriyor' cümlesini kuran bir çalışanın bu ifadesi bir tutumun hangi temel bileşenini doğrudan yansıtmaktadır?",
            "options": [
                "Bilişsel bileşen",
                "Davranışsal bileşen",
                "Duygusal bileşen",
                "Yansıtıcı bileşen",
                "Reaktif bileşen"
            ],
            "answer": 2,
            "explanation": "Tutumun duygusal (affective) bileşeni; bir kişiye, nesneye veya duruma karşı hissedilen duygu, his veya duygulanımsal tepkiyi yansıtır (hoşlanmama, öfke vb.).",
            "source": "Robbins & Judge Bölüm 3 · Tutumun Üç Bileşeni"
        },
        {
            "id": "v10-q13",
            "chapter": 3,
            "topic": "İş Tatminsizliğine Tepkiler: Çıkış (Exit)",
            "difficulty": "orta",
            "question": "Çalışma ortamındaki adaletsizliklerden ve terfi sisteminden derin bir tatminsizlik duyan bir kıdemli mühendis; yöneticileriyle tartışmaya girmemiş, şikayette bulunmamış, doğrudan gizlice başka şirketlere iş başvurusu yapmış ve yeni teklifi kabul ederek istifasını vermiştir. Mühendisin bu tepkisi EVLN modelinde hangi boyuttadır?",
            "options": [
                "Ses",
                "Çıkış",
                "Sadakat",
                "İhmal",
                "İntikam"
            ],
            "answer": 1,
            "explanation": "Çıkış (exit) tepkisi; aktif ve yıkıcı bir tepkidir. Birey tatminsizlik karşısında örgütten fiilen ayrılma yönünde davranış sergiler (istifa etme, başka iş arama).",
            "source": "Robbins & Judge Bölüm 3 · Tatminsizliğe Verilen Tepkiler: Çıkış"
        },
        {
            "id": "v10-q14",
            "chapter": 3,
            "topic": "Karşı Üretken İş Davranışları (CWB)",
            "difficulty": "orta",
            "question": "Çalışanların örgütün meşru çıkarlarına kasten zarar vermek amacıyla bilerek işi yavaşlatması, şirket ekipmanını sabote etmesi, şirket kaynaklarını zimmetine geçirmesi ya da iş arkadaşlarına iftira atması örgütsel davranışta hangi genel kavramla tanımlanır?",
            "options": [
                "Duygusal uyumsuzluk",
                "Geri çekilme davranışı",
                "Sosyal kaytarma",
                "Karşı üretken iş davranışı",
                "Bilişsel çelişki"
            ],
            "answer": 3,
            "explanation": "Karşı üretken iş davranışları (Counterproductive Work Behavior - CWB); çalışanların örgüte veya örgüt üyelerine bilerek ve isteyerek zarar verdiği sapkın eylemler bütünüdür.",
            "source": "Robbins & Judge Bölüm 3 · Karşı Üretken İş Davranışları"
        },
        {
            "id": "v10-q15",
            "chapter": 3,
            "topic": "İş Tatmini ve Müşteri Memnuniyeti",
            "difficulty": "kolay",
            "question": "Hizmet sektöründe (bankacılık, perakende, konaklama) çalışanların iş tatmini ile müşterilerin memnuniyet ve sadakati arasındaki ampirik ilişki hakkında aşağıdakilerden hangisi doğrudur?",
            "options": [
                "Çalışan tatmini arttıkça müşteri memnuniyeti düşmektedir.",
                "İki değişken arasında hiçbir korelasyon yoktur.",
                "Yalnızca çağrı merkezi çalışanlarında pozitif ilişki görülür.",
                "Müşteri memnuniyeti çalışanların iş tatminini hiçbir zaman etkilemez.",
                "İş tatmini yüksek çalışanlar müşterilere daha yardımsever ve güler yüzlü yaklaştığından müşteri memnuniyeti ve sadakati belirgin biçimde artar."
            ],
            "answer": 4,
            "explanation": "Hizmet sektöründe çalışanların tatmini doğrudan müşteriye yansır; memnun çalışanlar daha nazik, özenli ve pozitif hizmet vererek müşteri sadakatini ve memnuniyetini artırır.",
            "source": "Robbins & Judge Bölüm 3 · İş Tatmini ve Müşteri Memnuniyeti"
        },

        # Bölüm 4: Duygular ve Duygu Durumları (E, B, D, A, C)
        {
            "id": "v10-q16",
            "chapter": 4,
            "topic": "Duygusal Emek: Derin Rol",
            "difficulty": "orta",
            "question": "Bir müşteri hizmetleri temsilcisi, mağduriyet yaşayan ve çok kızgın olan bir müşteriye destek olurken sadece sahte bir gülümsemeyle rol yapmak yerine, kendisini samimiyetle müşterinin yerine koymuş, onun çaresizliğini içselleştirmiş ve gerçekten empati duyarak içsel hislerini müşteriye yardımcı olma arzusuna dönüştürmüştür. Temsilcinin bu çabası duygusal emeğin hangi boyutudur?",
            "options": [
                "Yüzeysel rol",
                "Duygusal uyumsuzluk",
                "Duygusal baskılama",
                "Sosyal mesafe",
                "Derin rol"
            ],
            "answer": 4,
            "explanation": "Derin rol (deep acting); çalışanın sergilemesi gereken duyguyu sadece taklit etmekle kalmayıp, içsel hislerini de bu duyguya uyarlamak için zihinsel ve duygusal çaba göstermesidir.",
            "source": "Robbins & Judge Bölüm 4 · Duygusal Emek: Derin Rol"
        },
        {
            "id": "v10-q17",
            "chapter": 4,
            "topic": "Duygusal Zekâ Savunucuları: Sezgisel Çekicilik",
            "difficulty": "orta",
            "question": "Duygusal zekânın önemini savunan araştırmacıların literatürde en çok vurguladığı 'sezgisel çekicilik' argümanı aşağıdakilerden hangisini savunur?",
            "options": [
                "Duygusal zekânın IQ testleriyle tamamen aynı sonuçları verdiğini",
                "Sosyal işaretleri doğru okuyan, başkalarının duygularını anlayan ve kendi hislerini yöneten kişilerin iş dünyasında başarılı olacağı düşüncesinin akla ve sezgiye son derece yatkın olduğunu",
                "Duygusal zekânın genetik olarak doğuştan geldiğini ve değiştirilemeyeceğini",
                "Duyguların iş kararlarından tamamen izole edilmesi gerektiğini",
                "Duygusal zekânın tüm şirketlerde zorunlu bir yasal kriter olduğunu"
            ],
            "answer": 1,
            "explanation": "Sezgisel çekicilik argümanı; başkalarının duygusal ipuçlarını sezebilen ve kendi duygularını kontrol edebilen kişilerin başarılı olacağı fikrinin mantıken son derece açık ve ikna edici olduğunu ifade eder.",
            "source": "Robbins & Judge Bölüm 4 · Duygusal Zekâyı Destekleyen Görüşler"
        },
        {
            "id": "v10-q18",
            "chapter": 4,
            "topic": "Günün Saati ve Pozitif Duygulanım",
            "difficulty": "zor",
            "question": "Robbins ve Judge'ın aktardığı geniş kapsamlı zaman-duygu araştırmalarına göre, çalışanların pozitif duygulanım (neşeli, coşkulu ve enerjik hissetme) seviyelerinin standart bir iş günü içindeki genel dalgalanma eğilimi nasıldır?",
            "options": [
                "Sabah uyanır uyanmaz en yüksek seviyededir ve akşama kadar sürekli düşer.",
                "Günün hiçbir saatinde değişmez, tamamen sabittir.",
                "Yalnızca gece saatlerinde zirve yapar.",
                "Sabah saatlerinde yükselmeye başlar, gün ortasında zirveye ulaşır ve akşam saatlerine doğru düşüşe geçer.",
                "Öğle yemeği sırasında aniden sıfıra iner."
            ],
            "answer": 3,
            "explanation": "Araştırmalar pozitif duygulanımın sabah saatlerinde tırmandığını, gün ortasında (öğle saatlerinde) zirveye ulaştığını ve akşamüstü saatlerinden itibaren azalmaya başladığını göstermektedir.",
            "source": "Robbins & Judge Bölüm 4 · Günün Saati ve Duygular"
        },
        {
            "id": "v10-q19",
            "chapter": 4,
            "topic": "Duygular ve Yaratıcı Karar Verme",
            "difficulty": "orta",
            "question": "Organizasyonlarda pozitif duygu durumlarının (örneğin mutluluk, heyecan ve neşe) çalışanların bilişsel süreçleri ve problem çözme becerileri üzerindeki etkisi hakkında hangisi bilimsel olarak doğrudur?",
            "options": [
                "Zihinsel esnekliği artırarak çalışanların yenilikçi, orijinal ve yaratıcı çözümler üretmesini kolaylaştırır.",
                "Çalışanların risk algısını yok ederek her zaman yıkıcı hatalar yapmalarına yol açar.",
                "Mantıksal düşünmeyi tamamen devre dışı bırakarak verimliliği düşürür.",
                "Yalnızca rutin ve tekrarlayan işlerde olumlu etki sağlar.",
                "Çalışanların meslektaşlarıyla işbirliği yapmasını engeller."
            ],
            "answer": 0,
            "explanation": "Pozitif duygu durumları bilişsel esnekliği genişletir, bireylerin yeni bilgi kalıplarını birleştirmesini destekler ve problem çözmede yaratıcılığı anlamlı biçimde artırır.",
            "source": "Robbins & Judge Bölüm 4 · Duyguların ÖD Uygulamaları: Yaratıcılık"
        },
        {
            "id": "v10-q20",
            "chapter": 4,
            "topic": "Ahlaki Duygular (Moral Emotions)",
            "difficulty": "zor",
            "question": "Bir çalışanın doğrudan kendi çıkarını ya da maddi durumunu hedef almasa bile, şirket içinde zayıf bir stajyere yapılan haksızlığı veya yöneticilerin yaptığı ahlak dışı bir suistimali gördüğünde hissettiği derin haklı öfke ve kınama hissi örgütsel davranışta hangi kavramla tanımlanır?",
            "options": [
                "Kişisel duygular",
                "Temel duygulanım",
                "Ahlaki duygular",
                "Bilişsel çelişki",
                "Yüzeysel rol"
            ],
            "answer": 2,
            "explanation": "Ahlaki duygular (moral emotions); bireyin doğrudan kendi çıkarıyla bağlantılı olmasa dahi ahlaki veya etik bir ihlal karşısında duyduğu haklı öfke, utanç veya sempati gibi hislerdir.",
            "source": "Robbins & Judge Bölüm 4 · Ahlaki Duygular"
        },

        # Bölüm 5: Kişilik ve Değerler (C, E, A, B, D)
        {
            "id": "v10-q21",
            "chapter": 5,
            "topic": "Büyük Beşli: Dışadönüklük ve Liderlik",
            "difficulty": "orta",
            "question": "Büyük Beşli kişilik özellikleri arasında; bireyin yönetsel pozisyonlarda lider olarak öne çıkmasını, sosyal etkileşimlerde inisiyatif almasını ve lider olarak algılanmasını en güçlü ve en tutarlı öngören kişilik boyutu hangisidir?",
            "options": [
                "Uyumluluk",
                "Duygusal denge",
                "Dışadönüklük",
                "Deneyime açıklık",
                "Makyavelizm"
            ],
            "answer": 2,
            "explanation": "Dışadönüklük (extraversion) boyutu; atılganlık, sosyallik ve enerji içerdiğinden lider olarak ortaya çıkmayı (liderlik algısını) en güçlü öngören boyuttur.",
            "source": "Robbins & Judge Bölüm 5 · Büyük Beşli ve Liderlik"
        },
        {
            "id": "v10-q22",
            "chapter": 5,
            "topic": "Özellik Aktivasyon Teorisi",
            "difficulty": "zor",
            "question": "Bireyin sahip olduğu belirli kişilik özelliklerinin ancak o özellikleri tetikleyen, ödüllendiren ya da dışa vurulmasını anlamlı kılan spesifik iş durumları, görev gereksinimleri ve ipuçları var olduğunda davranışa dönüşeceğini savunan çağdaş kişilik teorisi hangisidir?",
            "options": [
                "Durum gücü teorisi",
                "Bilişsel değerlendirme teorisi",
                "Beklenti teorisi",
                "Sosyal öğrenme teorisi",
                "Özellik aktivasyon teorisi"
            ],
            "answer": 4,
            "explanation": "Özellik aktivasyon teorisi (Trait Activation Theory - TAT); belirli kişilik özelliklerinin sergilenebilmesi için o özelliği aktive eden uygun durumsal ipuçlarının ve bağlamın gerektiğini savunur.",
            "source": "Robbins & Judge Bölüm 5 · Özellik Aktivasyon Teorisi"
        },
        {
            "id": "v10-q23",
            "chapter": 5,
            "topic": "Proaktif Kişilik",
            "difficulty": "orta",
            "question": "İş yerinde sorunların ortaya çıkmasını beklemeden gelecekteki fırsatları sezen, inisiyatif kullanarak yeni projeler başlatan ve karşılaştığı engellere rağmen çalıştığı kurumsal çevrede anlamlı değişimler yaratana kadar azimle çaba gösteren çalışan profili hangi kişilik kavramıyla tanımlanır?",
            "options": [
                "Proaktif kişilik",
                "A tipi kişilik",
                "Yüksek öz denetim",
                "Dışsal denetim odağı",
                "Makyavelist kişilik"
            ],
            "answer": 0,
            "explanation": "Proaktif kişilik (proactive personality); fırsatları yakalayan, inisiyatif alan, harekete geçen ve çevrelerinde anlamlı değişim yaratana kadar sebat eden bireyleri tanımlar.",
            "source": "Robbins & Judge Bölüm 5 · Diğer Kişilik Özellikleri: Proaktif Kişilik"
        },
        {
            "id": "v10-q24",
            "chapter": 5,
            "topic": "Rokeach Değer Anketi: Araçsal Değerler",
            "difficulty": "orta",
            "question": "Milton Rokeach tarafından geliştirilen Değer Anketinde; nihai amaçlara ulaşmada tercih edilen davranış tarzlarını, yöntemleri ve ahlaki ilkeleri (örneğin dürüst olmak, sorumluluk sahibi olmak, açık fikirli olmak, cesur olmak) tanımlayan değer kümesi hangisidir?",
            "options": [
                "Amaçsal değerler",
                "Araçsal değerler",
                "Stratejik değerler",
                "Kültürel değerler",
                "Evrensel değerler"
            ],
            "answer": 1,
            "explanation": "Araçsal (instrumental) değerler; bireyin arzu ettiği nihai (terminal) amaçlara ulaşmak için benimsediği ve uyguladığı davranış tarzları ve araç niteliğindeki ilkelerdir.",
            "source": "Robbins & Judge Bölüm 5 · Rokeach Değer Anketi: Araçsal Değerler"
        },
        {
            "id": "v10-q25",
            "chapter": 5,
            "topic": "Hofstede Kültür Boyutu: Toplulukçuluk",
            "difficulty": "kolay",
            "question": "Bireylerin kendilerini bağımsız bir aktörden ziyade ait oldukları sıkı sosyal grupların (aile, klan, çalışma takımı) bir parçası olarak gördükleri; grup çıkarlarının kişisel çıkarların önünde tutulduğu ve üyelerin birbirini koşulsuz gözettiği ulusal kültür boyutu Hofstede'ye göre hangisidir?",
            "options": [
                "Bireycilik",
                "Erillik",
                "Belirsizlikten kaçınma",
                "Toplulukçuluk",
                "Kısa vadeli yönelim"
            ],
            "answer": 3,
            "explanation": "Toplulukçuluk (collectivism); insanların parçası oldukları grubun diğer üyelerini gözettiği, grup sadakatinin ve ortak çıkarların bireysel başarının üzerinde tutulduğu kültürel çerçevedir.",
            "source": "Robbins & Judge Bölüm 5 · Hofstede: Toplulukçuluk"
        }
    ]
}

Path("docs/data/v10.json").write_text(json.dumps(v10_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("v10.json başarıyla oluşturuldu.")
