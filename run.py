import random
import matplotlib.pyplot as plt

wallet = 100000
how_much = [32510, 2300, 1820, 5210, 12370]
how_many = [0, 0, 0, 0, 0]
boss_news_bad = ['구속', '사망', '사임', '대통령과 비공개 면담', '인터넷 방송에서 논란 일으켜...', '시진핑과 대면 면담']
boss_news_good = ['로또 1등 당첨...당첨금 전액 사업에 투자', '대통령상 수상', '국회의원 당선', '인방 시작', '대통령선거 출마', '남북정상회담 배석기업인으로 참석예정']
company_news_good = ['정부가 선정한 유망기업 TOP 100 선정', '삼성전자에 부품 공급 확정', '대졸신입 연봉 6천만원...', '사회복지 사업 예산 확대', '독거노인 마스크 지원사업 시작']
company_news_bad = ['근무 중 노동자 사망', '공정거래위원회 제재받아...', '정경유착 의혹...청문회 예정', '국정농단 연루 의혹', 
                    '사내복지 논란', '구조조정 예정', '부실기업 평가 1위', '퇴사율 99% 달성', '급여지급 지연 드러나', '팀장이 내부 자금 횡령해', '공장에서 대형 화재 발생', '산업폐수 무단방류']
nothing = ['대표 숨쉰 채 발견...', '사내복지 내부평가 1위', '사내 학교 설치 확정', '대학법인 인수', '장학사업 시작', '페미니즘 지원사업 시작']
name = ['(주)운좋은금성', '(주)식회사', '(주)현아자동차', '(주)조선항공', '(주)비드고인']
jun_news = 0
jun_number = 1
howmuchbuy = [None, None, None, None, None]
jun_much = [0, 0, 0, 0, 0]
price = [[], [], [], [], []] #그래프 그리기용 
print('> 총 몇번의 회차를 돌리시겠습니까?')
for i in range(1, int(input())):
  
  r = random.randrange(1, 6)
  companynewsnumber = random.randrange(0, 5)
  for j in range(5):
    jun_much[j] = how_much[j]
    price[j].append(how_much[j])

  if r == 1:
    news = str(name[companynewsnumber]) + " 대표 " + str(random.choice(boss_news_bad))
  elif r == 2:
    news = str(name[companynewsnumber]) + " 대표 "+ str(random.choice(boss_news_good))
  elif r == 3:
      news = str(name[companynewsnumber]) + ", "+ str(random.choice(company_news_good))
  elif r == 4:
      news = str(name[companynewsnumber]) + ", "+ str(random.choice(company_news_bad))
  else:
      news = str(name[companynewsnumber]) + ", "+ str(random.choice(nothing))
  
  if jun_news == 1 or jun_news == 4:
      if random.randrange(1, 2) == 1:
        if random.randrange(1, 2) == 1:
          how_much[jun_number] -= random.randrange(int(how_much[jun_number]/1000), int(how_much[jun_number]/1))
  elif jun_news == 2 or jun_news == 3:
      if random.randrange(1, 2) == 1:
        if random.randrange(1, 2) == 1:
          how_much[jun_number] += random.randrange(int(how_much[jun_number]/1000), int(how_much[jun_number]/1))
  for p in range(5):
    if random.randrange(1, 2) == 1:
      randcom = p
      how_much[randcom] -= random.randrange(int(how_much[randcom]/1000), int(how_much[randcom]/100) + 1)
  

  jun_number = companynewsnumber
  jun_news = r
  for j in range(5):
    if how_much[j] <= 0:
      how_much[j] += -1 * how_much[j] + 1000
 
  print("현재 보유 현금 : ", wallet)  
  print("========<", i, "회차 시세 >=======")
  print("번호|  회사 명  | 시세 | 보유개수(매수 금액)")
  for k in range(5):
    if jun_much[k] > how_much[k]:
      print(k+1, " | ", name[k], " | ", how_much[k], "(▼", jun_much[k] - how_much[k],") | ", how_many[k], "(", howmuchbuy[k],")")
    elif jun_much[k] < how_much[k]:
      print(k+1, " | ", name[k], " | ", how_much[k], "(▲", how_much[k] - jun_much[k],") | ", how_many[k],"(", howmuchbuy[k],")")
    else:
      print(k+1, " | ", name[k], " | ", how_much[k], "(= ) | ", how_many[k],"(", howmuchbuy[k],")")
    
      
  print("========<", i, "회차 시세 >=======")
  print("최근 뉴스 : ", news)
  print("\n")
  print("> 매수는 1번, 매도는 2번을 입력하세요. ")
  buy_or_sell = int(input())
  success = False
  while success == False:
    if buy_or_sell == 1:
      print("> 매수할 회사의 번호를 입력하세요")
      buy_num = int(input())
      print("> ", name[buy_num - 1],"회사의 주식을 몇 주 매수하시겠습니까? (총 매수 가능 주식 : ", int(wallet/how_much[buy_num - 1]), ")")
      buy_num2 = int(input())
      if wallet >= how_much[buy_num-1] * buy_num2:
        wallet -= how_much[buy_num-1] * buy_num2
        how_many[buy_num-1] += buy_num2
        print("성공적으로 ", name[buy_num-1], "회사의 주식을 ", buy_num2, "주 매수했습니다.")
        howmuchbuy[buy_num-1] = how_much[buy_num - 1]
        success = True
      else:
        print("보유 현금이 부족합니다.")
    
    elif buy_or_sell == 2:
      print("> 매도할 회사의 번호를 입력하세요")
      sell_num = int(input())
      print("> ", name[sell_num - 1],"회사의 주식을 몇 주 매도하시겠습니까? (총 매도 가능 주식 : ", how_many[sell_num - 1], ")")
      sell_num2 = int(input())
      if how_many[sell_num - 1] >= sell_num2:
        how_many[sell_num - 1] -= sell_num2
        print("성공적으로 ", name[sell_num-1], "회사의 주식을 ", sell_num2, "주 매도했습니다.")
        wallet += how_much[sell_num - 1] * sell_num2
        howmuchbuy[sell_num-1] = None
        success = True
      else:
        print("보유 주식이 부족합니다.")
    else:
      print("다시 입력해 주세요.")
      i -= 1
      buy_or_sell = 0
      break
sum = 0
for i in range(5):
    sum += how_much[i] * how_many[i]
sum += wallet

print("========게임 종료========")
print("시작 금액 : 100000원")
print("현재 보유 금액 : ", sum,"원")
