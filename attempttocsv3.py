import os
import xml.etree.ElementTree as ET

# 小テスト一覧を取得(課題とクイズ両方含む)
quizes=[]
for f in os.listdir('activities'):
    if f.startswith('quiz_'):
        quizes.append(f)
#print(quizes)
    
for q in quizes:
    xml = ET.parse('activities/' + q + '/quiz.xml')
    root = xml.getroot()
    quiz = root.findall('quiz')[0]
    qname = quiz.findall('name')[0].text
    # 課題の場合だけ以下を処理
    if qname.startswith('課題'):
        timeopen = quiz.findall('timeopen')[0].text # 課題公開日時
        print(q, qname, timeopen)
        attempts = quiz.findall('attempts')[0] # 受験データを探す
        for g in attempts:
            userid = g.findall('userid')[0].text # ユーザ
            num = g.findall('attemptnum')[0].text # 何回目の受験?
            grade = g.findall('sumgrades')[0].text # 点数
            # 点数がいるもののみ以下を処理
            if grade != '$@NULL@$':
                time = g.findall('timefinish')[0].text # 受験日時
                print('"{0}",{1},{2},{3},{4}'.format(qname, userid, num, grade, int(time) - int(timeopen)))
