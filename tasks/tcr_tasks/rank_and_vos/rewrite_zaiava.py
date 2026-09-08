# -*- coding: utf-8 -*-
"""Produce Zaiava_zvannia.docx from Dmytro's own template.

Takes ../registry_application/source/Заява.docx and replaces the text of named
paragraphs, keeping each paragraph's own w:pPr and the w:rPr of its first run, then
normalises the whole document to Times New Roman 12 pt, 1.5 line spacing, justified.

Never rebuild this document through code/build/build_docx.py — the builder imposes its
own layout and destroys the original's addressee block, centred title and spacing.

    PYTHONUTF8=1 venv/Scripts/python.exe tasks/tcr_tasks/rank_and_vos/rewrite_zaiava.py <src.docx> <dst.docx>
"""
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

src, dst = sys.argv[1], sys.argv[2]

# --- text: paragraph index in the source -> replacement (""  blanks the paragraph) ---
NEW = {
 1: "<НАЗВА> районного (міського) територіального центру комплектування та соціальної підтримки",
27: "Про внесення до Єдиного державного реєстру призовників, військовозобов’язаних та резервістів відомостей про військове звання",
29: "Я, ПІБ, перебуваю на військовому обліку у <НАЗВА> районному (міському) територіальному центрі комплектування та соціальної підтримки. Військової служби, навчальних зборів та фахової військової підготовки я не проходив. (дата) мені виповнилося 25 років.",
31: "Проте (дата) при формуванні електронного військово-облікового документа мною було виявлено, що мене взято на військовий облік військовозобов’язаних, однак відомості про моє військове звання відсутні",
32: "у Єдиному державному реєстрі призовників, військовозобов’язаних та резервістів.",
34: "Пунктом 79 Порядку організації та ведення військового обліку призовників, військовозобов’язаних та резервістів, затвердженого постановою Кабінету Міністрів України від 30 грудня 2022 року № 1487, встановлено, що районні (міські) територіальні центри комплектування та соціальної підтримки організовують внесення до Реєстру інформації про зняття призовників з військового обліку призовників та взяття їх на облік військовозобов’язаних з одночасним присвоєнням військового звання «солдат (матрос) запасу».",
36: "Таке внесення здійснюється у тридцятиденний строк після досягнення призовником 25-річного віку та без виклику особи до територіального центру комплектування та соціальної підтримки.",
37: "Отже, взяття на облік військовозобов’язаних та присвоєння військового звання «солдат (матрос) запасу» становлять єдину дію, здійснення якої не поставлено в залежність від проходження військової служби, базової загальновійськової підготовки, військово-лікарської комісії чи наявності військового квитка.",
38: "Взяття на облік військовозобов’язаних щодо мене здійснено, відомості про військове звання до Реєстру не внесено.",
39: "",
41: "Частиною восьмою статті 5 Закону України «Про Єдиний державний реєстр призовників, військовозобов’язаних та резервістів» визначено, що органами ведення Реєстру є Міністерство оборони України, районні (об’єднані районні), міські (районні у місті, об’єднані міські) територіальні центри комплектування та соціальної підтримки, центри рекрутингу Збройних Сил України, Центральне управління Служби безпеки України та регіональні органи Служби безпеки України, відповідні підрозділи розвідувальних органів України.",
42: "Пунктом 43 Порядку ведення Єдиного державного реєстру призовників, військовозобов’язаних та резервістів, затвердженого постановою Кабінету Міністрів України від 29 липня 2026 року № 981, встановлено, що виправлення недостовірних відомостей Реєстру та зміна облікових даних здійснюються за результатами розгляду відповідної мотивованої заяви, яка подається до органів ведення Реєстру.",
56: "Внести до Єдиного державного реєстру призовників, військовозобов’язаних та резервістів відомості про присвоєне мені військове звання «солдат (матрос) запасу» та про розряд запасу, а також забезпечити відображення цих відомостей в електронному військово-обліковому документі. Про результати розгляду цієї заяви повідомити письмово на зазначені вище адресу для листування та електронну адресу.",
}

# --- formatting: Times New Roman 12 pt, 1.5 spacing, justified body ---
FONT = ('<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
        'w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/>')
SPACING = '<w:spacing w:line="360" w:lineRule="auto"/>'
# the addressee/applicant block (0-22) and the short standalone lines keep their own
# alignment; the title stays centred; everything else is justified.
KEEP_ALIGNMENT = set(range(0, 23)) | {26, 27, 54, 59, 63}

zin = zipfile.ZipFile(src)
doc = zin.read("word/document.xml").decode("utf-8")

paras = list(re.finditer(r"<w:p[ >].*?</w:p>", doc, re.S))
assert len(paras) == 67, "source template changed: %d paragraphs" % len(paras)


def set_runs(p_xml, text):
    """Replace every run with one run carrying the first run's rPr and `text`."""
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p_xml, re.S)
    rpr = re.search(r"<w:r[ >].*?(<w:rPr>.*?</w:rPr>)", p_xml, re.S)
    rpr = rpr.group(1) if rpr else ""
    body = ""
    if text:
        body = '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, escape(text))
    return re.match(r"<w:p[^>]*>", p_xml).group(0) + (ppr.group(0) if ppr else "") + body + "</w:p>"


def restyle(p_xml, justify):
    """Force the font on every run and the spacing (and alignment) on the paragraph."""
    def fix_run(m):
        run = m.group(0)
        if "<w:rPr>" in run:
            run = re.sub(r"<w:rFonts[^>]*/>|<w:sz w:val=\"\d+\"/>|<w:szCs w:val=\"\d+\"/>", "", run)
            run = run.replace("<w:rPr>", "<w:rPr>" + FONT, 1)
        else:
            run = re.sub(r"(<w:r[ >][^>]*>|<w:r>)", r"\1<w:rPr>" + FONT + "</w:rPr>", run, count=1)
        return run

    p_xml = re.sub(r"<w:r[ >].*?</w:r>", fix_run, p_xml, flags=re.S)

    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p_xml, re.S)
    if ppr:
        new = re.sub(r"<w:spacing[^>]*/>", "", ppr.group(0))
        if justify:
            new = re.sub(r"<w:jc[^>]*/>", "", new)
        new = new.replace("<w:pPr>", "<w:pPr>" + SPACING + ('<w:jc w:val="both"/>' if justify else ""), 1)
        p_xml = p_xml.replace(ppr.group(0), new, 1)
    else:
        inject = "<w:pPr>" + SPACING + ('<w:jc w:val="both"/>' if justify else "") + "</w:pPr>"
        p_xml = re.sub(r"(<w:p[^>]*>)", r"\1" + inject, p_xml, count=1)
    return p_xml


out, last = [], 0
for i, m in enumerate(paras):
    p = m.group(0)
    if i in NEW:
        p = set_runs(p, NEW[i])
    p = restyle(p, justify=i not in KEEP_ALIGNMENT)
    out.append(doc[last:m.start()])
    out.append(p)
    last = m.end()
doc = "".join(out) + doc[last:]
doc = doc.replace("2024 року", "2026 року")

# document defaults, so anything typed into the file later inherits the same font
styles = zin.read("word/styles.xml").decode("utf-8")
styles = re.sub(r"<w:rFonts[^>]*/>", '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
                'w:eastAsia="Times New Roman" w:cs="Times New Roman"/>', styles, count=1)
styles = re.sub(r"<w:sz w:val=\"\d+\"/>", '<w:sz w:val="24"/>', styles, count=1)
styles = re.sub(r"<w:szCs w:val=\"\d+\"/>", '<w:szCs w:val="24"/>', styles, count=1)

tmp = dst + ".tmp"
zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename == "word/document.xml":
        data = doc.encode("utf-8")
    elif it.filename == "word/styles.xml":
        data = styles.encode("utf-8")
    zout.writestr(it, data)
zout.close()
zin.close()
os.replace(tmp, dst)
print("wrote", dst, os.path.getsize(dst), "bytes")
