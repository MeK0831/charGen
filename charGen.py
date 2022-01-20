import random


# ===== DB bellow =======

#species
species = {'mankind': ['human','giant','hobbit','valkyria','elf','darkelf','witch','clone'],
           'fairykind':['seirei','dryad','dwarf','fairy','banshes'],
           'undeadkind':['zombies','ghoul','vampire','dullahan'],
           'monsterkind':['troll','orc','oni','dokkebi','halfmonster','slime','tentacle'],
           'furrykind':['kumiho','lizardman','furry','lamia','insectoid','mermaid','arachne','hapi','seiren','minotauros',
                        'satyr','werewolf','kitty','bunny','doggo','dragonia','octopus'],
           'godkind':['angel','fallenangel','demon','reaper','god','demigod','succubus','halfdemon'],
           'machinekind':['cyborg','humanoid','furriroid'],
           'servantkind':['servant'],
           'alienkind':['alien']}

#type and relation
type = ['메스가키','누나','loli','여동생','MILF','동갑']
relation = ['소꿉친구','라이벌','적대관계','상사','부하직원','주인','노예','동료','갸루']

#personality
personality = ['얀데레','츤데레','메가데레','쿨','시니컬','활동적','히키코모리','찐','차분한','어른스러운','똑똑한','멍청한','순진한','청순한','애교넘치는','보이쉬','용감한','겁이 많은','교활한','여우같은']

#hairstyle
hstyle = ['포니테일','단발','트윈테일','칼단발','픽시컷','히메컷','숏컷','웨이브','직 장발','드릴','땋은머리','똥머리','반묶음']

#job
job = ['간호사','교사','조교','무직','회사원','학생','연구원','의사','경찰','교도관','군인','공무원','약사','아나운서','연예인','아이돌','가수','스튜어디스','개발자','성우',
       '일러스트레이터','만화가','아르바이트','건설노동자','생산직','메이드','CEO','사진가','언론인','농부',
       '요리사','프로게이머','해커','프로듀서','운동선수','탐험가','사육사','학자','파일럿','코미디언','외교관',
       '레이싱모델','치어리더','마술사','모델','화가','정치인','종교인','무당','무술가','대장장이','레이서','구급대원',
       '묘지기','기술자','매니져','비서','건달','주술사','검사','마법사','신관','궁수','도적','사무라이','음양사','주술사','소환사','브리더','무녀','흑마법사','거너','랜서','격투가',
       '닌자','용기사','흑기사','인형사','모험가','상인','기병','버서커','기사']

#boobsize
bsize = ['AAA','A','B','C','D','E','F','G','H','K']

# ===== func bellow =====

def get_species(): # 종족 선택
       keys_species = list(species.keys()) #키를 리스트로 저장
       key_species = random.choice(keys_species) #랜덤으로 키 추출
       #print (key_species)
       var_species = random.choice(list(species.get(key_species))) # 랜덤으로 선택된 키의 리스트로부터 종 추출
       return key_species, var_species

def get_type(): # 타입 선택
       var_type = random.choice(type)
       return var_type

def get_relation(): # 포지션 선택
       var_relation = random.choice(relation)
       return var_relation

def get_personality(): # 성격 선택
       var_personality = random.choice(personality)
       return var_personality

def get_hstyle(): # 헤어 스타일
       var_hstyle = random.choice(hstyle)
       return var_hstyle

def get_job(): # 직업 선택
       var_job = random.choice(job)
       return var_job

def get_bsize(): # 가슴크기 선택
       var_bsize = random.choice(bsize)
       return var_bsize

def get_randcolor(): # 랜덤 컬러 선택
       
       r = random.randrange(0,256,1)
       g = random.randrange(0,256,1)
       b = random.randrange(0,256,1)

       r = str(hex(r)).replace("0x","").zfill(2)
       g = str(hex(g)).replace("0x","").zfill(2)
       b = str(hex(b)).replace("0x","").zfill(2)

       randcolor = r+g+b
       return randcolor

def get_hcolor(): # 머리카락 색 선택
       var_hcolor = hex(int(get_randcolor(),16))
       return var_hcolor

def get_ecolor(): # 눈 색 선택
       var_ecolor = hex(int(get_randcolor(),16))
       return var_ecolor


# ===== 예제 =====
if __name__ == '__main__':
       print('종족: ', get_species())
       print('타입: ', get_type())
       print('관계: ', get_relation())
       print('성격: ', get_personality())
       print('직업: ', get_job())
       print('헤어 스타일: ', get_hstyle())
       print('헤어 색상: ', get_hcolor())
       print('눈 색상: ', get_ecolor())
       print('가슴 크기: ', get_bsize())