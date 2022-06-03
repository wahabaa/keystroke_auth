import unittest
import requests
import mysql.connector


def validate_request_body(keystroke, user='100', sig='814fe8c2123ab9ad26728ebbc71596a0'):
    '''
    Request body for the /verify endpoint
    :param keystroke:
    :param user:
    :param sig:
    :return: data
    '''
    data = {'user': user, 'customer_sig': sig, 'k_username': keystroke[0], 'k_pwd': keystroke[1]}
    return data


def notify_request_body(isPassed, user='100'):
    '''
    Request body for the /notify endpoint
    :param isPassed:
    :param user:
    :return: data
    '''
    data = {'user': user, 'isPassed': isPassed}
    return data


def clean_DB(user='100'):
    '''
    Clear old records in DB
    :param user:
    :return:
    '''
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cheachoo",
        database="soteria"
    )
    try:
        mycursor = mydb.cursor()
        sql_1 = "DELETE FROM keystrokes WHERE user = " + user
        sql_2 = "DELETE FROM reject_keys WHERE user = " + user
        mycursor.execute(sql_1)
        mycursor.execute(sql_2)
        mydb.commit()
    except Exception as e:
        mydb.rollback()


class Test_api(unittest.TestCase):
    API_URL = 'https://8f1e-67-249-20-200.ngrok.io'
    VALIDATE_ENDPOINT = '{}/validate'.format(API_URL)
    NOTIFY_ENDPOINT = '{}/notify'.format(API_URL)
    CODE_200 = 200
    CODE_400 = 400
    CODE_401 = 401
    VERIFY_RESPONSE_200 = {"code": 200, "status": "Building template", "user": "100"}
    VERIFY_RESPONSE_200_APPROVED = {"code": 200, "status": "Approved", "user": "100"}
    VERIFY_RESPONSE_400 = {"code": 400, "status": "Denied", "user": "100"}
    VERIFY_RESPONSE_401 = {'error': 'Invalid input', "code": 401}
    NOTIFY_RESPONSE_200 = {"user": "100", "status": "Successful", "code": 200}
    NOTIFY_RESPONSE_401a = {'error': 'Nothing to delete', "code": 401}
    NOTIFY_RESPONSE_401b = {'error': 'Invalid input', "code": 401}
    K_USERNAME_1 = '[{"kn":"a","r":0,"ts":1654101118875,"wn":"username"},{"kn":"a","r":1,"ts":1654101118931,"wn":"username"},{"kn":"n","r":0,"ts":1654101119021,"wn":"username"},{"kn":"n","r":1,"ts":1654101119100,"wn":"username"},{"kn":"u","r":0,"ts":1654101119246,"wn":"username"},{"kn":"u","r":1,"ts":1654101119302,"wn":"username"},{"kn":"m","r":0,"ts":1654101119494,"wn":"username"},{"kn":"m","r":1,"ts":1654101119561,"wn":"username"},{"kn":"i","r":0,"ts":1654101119696,"wn":"username"},{"kn":"i","r":1,"ts":1654101119730,"wn":"username"},{"kn":"g","r":0,"ts":1654101119933,"wn":"username"},{"kn":"g","r":1,"ts":1654101119977,"wn":"username"},{"kn":"h","r":0,"ts":1654101120124,"wn":"username"},{"kn":"h","r":1,"ts":1654101120180,"wn":"username"},{"kn":"t","r":0,"ts":1654101120326,"wn":"username"},{"kn":"t","r":1,"ts":1654101120394,"wn":"username"},{"kn":"y","r":0,"ts":1654101120551,"wn":"username"},{"kn":"y","r":1,"ts":1654101120607,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101120844,"wn":"username"}]'
    K_PWD_1 = '[{"kn":"Tab","r":1,"ts":1654101120899,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101121394,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101121461,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101121608,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101121675,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101121855,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101121900,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101122047,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101122136,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101122294,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101122361,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101122508,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101122575,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101122744,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101122812,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101123149,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101123205,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101123386,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101123430,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101123610,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101123678,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101123824,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101123914,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101124038,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101124116,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101124263,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101124341,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101124465,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101124533,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101124994,"wn":"pwd"}]'
    K_USERNAME_2 = '[{"kn":"a","r":0,"ts":1654101131003,"wn":"username"},{"kn":"a","r":1,"ts":1654101131070,"wn":"username"},{"kn":"n","r":0,"ts":1654101131194,"wn":"username"},{"kn":"n","r":1,"ts":1654101131261,"wn":"username"},{"kn":"u","r":0,"ts":1654101131419,"wn":"username"},{"kn":"u","r":1,"ts":1654101131475,"wn":"username"},{"kn":"m","r":0,"ts":1654101131655,"wn":"username"},{"kn":"m","r":1,"ts":1654101131722,"wn":"username"},{"kn":"i","r":0,"ts":1654101131858,"wn":"username"},{"kn":"i","r":1,"ts":1654101131914,"wn":"username"},{"kn":"g","r":0,"ts":1654101132105,"wn":"username"},{"kn":"g","r":1,"ts":1654101132161,"wn":"username"},{"kn":"h","r":0,"ts":1654101132296,"wn":"username"},{"kn":"h","r":1,"ts":1654101132352,"wn":"username"},{"kn":"t","r":0,"ts":1654101132533,"wn":"username"},{"kn":"t","r":1,"ts":1654101132589,"wn":"username"},{"kn":"y","r":0,"ts":1654101132735,"wn":"username"},{"kn":"y","r":1,"ts":1654101132814,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101132983,"wn":"username"}]'
    K_PWD_2 = '[{"kn":"Tab","r":1,"ts":1654101133060,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101133612,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101133657,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101133826,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101133882,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101134062,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101134106,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101134287,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101134343,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101134512,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101134568,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101134737,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101134815,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101134950,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101135029,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101135401,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101135434,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101135614,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101135670,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101135850,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101135895,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101136064,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101136131,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101136278,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101136356,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101136503,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101136559,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101136717,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101136784,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101137324,"wn":"pwd"}]'
    K_USERNAME_3 = '[{"kn":"a","r":0,"ts":1654101143254,"wn":"username"},{"kn":"a","r":1,"ts":1654101143310,"wn":"username"},{"kn":"n","r":0,"ts":1654101143423,"wn":"username"},{"kn":"n","r":1,"ts":1654101143501,"wn":"username"},{"kn":"u","r":0,"ts":1654101143648,"wn":"username"},{"kn":"u","r":1,"ts":1654101143715,"wn":"username"},{"kn":"m","r":0,"ts":1654101143907,"wn":"username"},{"kn":"m","r":1,"ts":1654101143962,"wn":"username"},{"kn":"i","r":0,"ts":1654101144120,"wn":"username"},{"kn":"i","r":1,"ts":1654101144165,"wn":"username"},{"kn":"g","r":0,"ts":1654101144357,"wn":"username"},{"kn":"g","r":1,"ts":1654101144412,"wn":"username"},{"kn":"h","r":0,"ts":1654101144548,"wn":"username"},{"kn":"h","r":1,"ts":1654101144615,"wn":"username"},{"kn":"t","r":0,"ts":1654101144784,"wn":"username"},{"kn":"t","r":1,"ts":1654101144840,"wn":"username"},{"kn":"y","r":0,"ts":1654101144987,"wn":"username"},{"kn":"y","r":1,"ts":1654101145054,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101145392,"wn":"username"}]'
    K_PWD_3 = '[{"kn":"Tab","r":1,"ts":1654101145469,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101145863,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101145919,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101146088,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101146144,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101146302,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101146358,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101146527,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101146594,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101146763,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101146830,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101146977,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101147044,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101147179,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101147258,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101147618,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101147663,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101147832,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101147899,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101148079,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101148135,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101148293,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101148360,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101148507,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101148585,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101148709,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101148776,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101148934,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101148990,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101149373,"wn":"pwd"}]'
    K_USERNAME_4 = '[{"kn":"a","r":0,"ts":1654101155742,"wn":"username"},{"kn":"a","r":1,"ts":1654101155820,"wn":"username"},{"kn":"n","r":0,"ts":1654101155922,"wn":"username"},{"kn":"n","r":1,"ts":1654101155989,"wn":"username"},{"kn":"u","r":0,"ts":1654101156124,"wn":"username"},{"kn":"u","r":1,"ts":1654101156180,"wn":"username"},{"kn":"m","r":0,"ts":1654101156360,"wn":"username"},{"kn":"m","r":1,"ts":1654101156428,"wn":"username"},{"kn":"i","r":0,"ts":1654101156574,"wn":"username"},{"kn":"i","r":1,"ts":1654101156619,"wn":"username"},{"kn":"g","r":0,"ts":1654101156799,"wn":"username"},{"kn":"g","r":1,"ts":1654101156855,"wn":"username"},{"kn":"h","r":0,"ts":1654101156979,"wn":"username"},{"kn":"h","r":1,"ts":1654101157057,"wn":"username"},{"kn":"t","r":0,"ts":1654101157204,"wn":"username"},{"kn":"t","r":1,"ts":1654101157271,"wn":"username"},{"kn":"y","r":0,"ts":1654101157418,"wn":"username"},{"kn":"y","r":1,"ts":1654101157474,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101157632,"wn":"username"}]'
    K_PWD_4 = '[{"kn":"Tab","r":1,"ts":1654101157709,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101158249,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101158294,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101158441,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101158530,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101158688,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101158733,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101158891,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101158969,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101159082,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101159183,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101159307,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101159385,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101159510,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101159588,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101159914,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101159970,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101160139,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101160195,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101160353,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101160409,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101160567,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101160645,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101160781,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101160848,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101160983,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101161050,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101161197,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101161253,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101161872,"wn":"pwd"}]'
    K_USERNAME_5 = '[{"kn":"a","r":0,"ts":1654101165507,"wn":"username"},{"kn":"a","r":1,"ts":1654101165574,"wn":"username"},{"kn":"n","r":0,"ts":1654101165687,"wn":"username"},{"kn":"n","r":1,"ts":1654101165754,"wn":"username"},{"kn":"u","r":0,"ts":1654101165867,"wn":"username"},{"kn":"u","r":1,"ts":1654101165923,"wn":"username"},{"kn":"m","r":0,"ts":1654101166103,"wn":"username"},{"kn":"m","r":1,"ts":1654101166159,"wn":"username"},{"kn":"i","r":0,"ts":1654101166283,"wn":"username"},{"kn":"i","r":1,"ts":1654101166327,"wn":"username"},{"kn":"g","r":0,"ts":1654101166508,"wn":"username"},{"kn":"g","r":1,"ts":1654101166575,"wn":"username"},{"kn":"h","r":0,"ts":1654101166711,"wn":"username"},{"kn":"h","r":1,"ts":1654101166766,"wn":"username"},{"kn":"t","r":0,"ts":1654101166924,"wn":"username"},{"kn":"t","r":1,"ts":1654101166991,"wn":"username"},{"kn":"y","r":0,"ts":1654101167127,"wn":"username"},{"kn":"y","r":1,"ts":1654101167183,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101167397,"wn":"username"}]'
    K_PWD_5 = '[{"kn":"Tab","r":1,"ts":1654101167463,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101167981,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101168037,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101168183,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101168250,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101168408,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101168475,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101168622,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101168700,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101168824,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101168892,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101169027,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101169094,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101169241,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101169308,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101169623,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101169690,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101169848,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101169938,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101170073,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101170129,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101170276,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101170343,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101170489,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101170557,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101170714,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101170770,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101170906,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101170984,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101171434,"wn":"pwd"}]'
    K_USERNAME_6 = '[{"kn":"a","r":0,"ts":1654101175217,"wn":"username"},{"kn":"a","r":1,"ts":1654101175294,"wn":"username"},{"kn":"n","r":0,"ts":1654101175407,"wn":"username"},{"kn":"n","r":1,"ts":1654101175474,"wn":"username"},{"kn":"u","r":0,"ts":1654101175609,"wn":"username"},{"kn":"u","r":1,"ts":1654101175677,"wn":"username"},{"kn":"m","r":0,"ts":1654101175857,"wn":"username"},{"kn":"m","r":1,"ts":1654101175924,"wn":"username"},{"kn":"i","r":0,"ts":1654101176059,"wn":"username"},{"kn":"i","r":1,"ts":1654101176115,"wn":"username"},{"kn":"g","r":0,"ts":1654101176296,"wn":"username"},{"kn":"g","r":1,"ts":1654101176352,"wn":"username"},{"kn":"h","r":0,"ts":1654101176487,"wn":"username"},{"kn":"h","r":1,"ts":1654101176565,"wn":"username"},{"kn":"t","r":0,"ts":1654101176700,"wn":"username"},{"kn":"t","r":1,"ts":1654101176768,"wn":"username"},{"kn":"y","r":0,"ts":1654101176903,"wn":"username"},{"kn":"y","r":1,"ts":1654101176970,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101177128,"wn":"username"}]'
    K_PWD_6 = '[{"kn":"Tab","r":1,"ts":1654101177206,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101177689,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101177746,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101177903,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101177971,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101178117,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101178173,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101178342,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101178420,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101178533,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101178612,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101178758,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101178825,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101178983,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101179028,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101179332,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101179388,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101179557,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101179613,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101179793,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101179860,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101180007,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101180086,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101180198,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101180265,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101180401,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101180468,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101180603,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101180659,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101181143,"wn":"pwd"}]'
    K_USERNAME_7 = '[{"kn":"a","r":0,"ts":1654101792475,"wn":"username"},{"kn":"a","r":1,"ts":1654101792564,"wn":"username"},{"kn":"n","r":0,"ts":1654101792992,"wn":"username"},{"kn":"n","r":1,"ts":1654101793059,"wn":"username"},{"kn":"u","r":0,"ts":1654101793476,"wn":"username"},{"kn":"u","r":1,"ts":1654101793532,"wn":"username"},{"kn":"m","r":0,"ts":1654101793723,"wn":"username"},{"kn":"m","r":1,"ts":1654101793802,"wn":"username"},{"kn":"i","r":0,"ts":1654101794353,"wn":"username"},{"kn":"i","r":1,"ts":1654101794420,"wn":"username"},{"kn":"g","r":0,"ts":1654101794623,"wn":"username"},{"kn":"g","r":1,"ts":1654101794691,"wn":"username"},{"kn":"h","r":0,"ts":1654101794815,"wn":"username"},{"kn":"h","r":1,"ts":1654101794882,"wn":"username"},{"kn":"t","r":0,"ts":1654101795298,"wn":"username"},{"kn":"t","r":1,"ts":1654101795399,"wn":"username"},{"kn":"y","r":0,"ts":1654101795658,"wn":"username"},{"kn":"y","r":1,"ts":1654101795714,"wn":"username"},{"kn":"Tab","r":0,"ts":1654101796198,"wn":"username"}]'
    K_PWD_7 = '[{"kn":"Tab","r":1,"ts":1654101796343,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101797277,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101797345,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101797873,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101797952,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101798413,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101798481,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101798751,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101798829,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101799381,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101799482,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101799741,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101799808,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101799977,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101800056,"wn":"pwd"},{"kn":"u","r":0,"ts":1654101800438,"wn":"pwd"},{"kn":"u","r":1,"ts":1654101800506,"wn":"pwd"},{"kn":"n","r":0,"ts":1654101800832,"wn":"pwd"},{"kn":"n","r":1,"ts":1654101800899,"wn":"pwd"},{"kn":"i","r":0,"ts":1654101801215,"wn":"pwd"},{"kn":"i","r":1,"ts":1654101801282,"wn":"pwd"},{"kn":"l","r":0,"ts":1654101801699,"wn":"pwd"},{"kn":"l","r":1,"ts":1654101801766,"wn":"pwd"},{"kn":"a","r":0,"ts":1654101801946,"wn":"pwd"},{"kn":"a","r":1,"ts":1654101802058,"wn":"pwd"},{"kn":"g","r":0,"ts":1654101802362,"wn":"pwd"},{"kn":"g","r":1,"ts":1654101802441,"wn":"pwd"},{"kn":"1","r":0,"ts":1654101802587,"wn":"pwd"},{"kn":"1","r":1,"ts":1654101802666,"wn":"pwd"},{"kn":"Enter","r":0,"ts":1654101804421,"wn":"pwd"}]'
    ALL_KEYS = [[K_USERNAME_1, K_PWD_1], [K_USERNAME_2, K_PWD_2], [K_USERNAME_3, K_PWD_3], [K_USERNAME_4, K_PWD_4], [K_USERNAME_5, K_PWD_5], [K_USERNAME_6, K_PWD_6], [K_USERNAME_7, K_PWD_7]]

    '''BUILDING TEMPLATE (PROFILE)----------------------------------------------------------------------------------'''
    # POST REQUEST to /verify for the first five login attempt
    def test_1_building_template(self):
        clean_DB() # Clear old records
        for i in range(5):
            r = requests.post(url=Test_api.VALIDATE_ENDPOINT, json=validate_request_body(Test_api.ALL_KEYS[i]))
            self.assertEqual(r.status_code, Test_api.CODE_200)
            self.assertDictEqual(r.json(), Test_api.VERIFY_RESPONSE_200)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''SUCCESSFUL KEYSTROKE AUTH -----------------------------------------------------------------------------------'''
    # POST REQUEST to /verify for successful keystroke authentication (sixth login attempt)
    def test_2_successful_keystroke_auth(self):
        r = requests.post(url=Test_api.VALIDATE_ENDPOINT, json=validate_request_body([Test_api.K_USERNAME_6, Test_api.K_PWD_6]))
        self.assertEqual(r.status_code, Test_api.CODE_200)
        self.assertDictEqual(r.json(), Test_api.VERIFY_RESPONSE_200_APPROVED)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''FAILED KEYSTROKE AUTH ---------------------------------------------------------------------------------------'''
    # POST REQUEST to /verify for failed keystroke authentication (seventh login attempt)
    def test_3_failed_keystroke_auth(self):
        r = requests.post(url=Test_api.VALIDATE_ENDPOINT, json=validate_request_body([Test_api.K_USERNAME_7, Test_api.K_PWD_7]))
        self.assertEqual(r.status_code, Test_api.CODE_400)
        self.assertDictEqual(r.json(), Test_api.VERIFY_RESPONSE_400)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''INVALID INPUT------------------------------------------------------------------------------------------------'''
    # POST REQUEST to /verify for invalid input (eighth login attempt)
    def test_4_invalid_input_entered(self):
        r = requests.post(url=Test_api.VALIDATE_ENDPOINT, json=validate_request_body(['', '']))
        self.assertEqual(r.status_code, Test_api.CODE_401)
        self.assertDictEqual(r.json(), Test_api.VERIFY_RESPONSE_401)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''UPDATE PROFILE SUCCESSFULLY ---------------------------------------------------------------------------------'''
    # POST REQUEST to /notify after user passed 2FA
    def test_5_update_profile_successfully(self):
        r = requests.post(url=Test_api.NOTIFY_ENDPOINT, json=notify_request_body(True))
        self.assertEqual(r.status_code, Test_api.CODE_200)
        self.assertDictEqual(r.json(), Test_api.NOTIFY_RESPONSE_200)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''FAILED TO UPDATE PROFILE (NOTHING TO DELETE) ----------------------------------------------------------------'''
    # POST REQUEST to /notify after user passed 2FA
    def test_6_failed_to_update_profile(self):
        r = requests.post(url=Test_api.NOTIFY_ENDPOINT, json=notify_request_body(False))
        self.assertEqual(r.status_code, Test_api.CODE_401)
        self.assertDictEqual(r.json(), Test_api.NOTIFY_RESPONSE_401a)
    '''-------------------------------------------------------------------------------------------------------------'''

    '''FAILED TO UPDATE PROFILE (INVALID INPUT)---------------------------------------------------------------------'''
    # POST REQUEST to /notify after user passed 2FA
    def test_7_failed_to_update_profile(self):
        r = requests.post(url=Test_api.NOTIFY_ENDPOINT, json={})
        self.assertEqual(r.status_code, Test_api.CODE_401)
        self.assertDictEqual(r.json(), Test_api.NOTIFY_RESPONSE_401b)
    '''-------------------------------------------------------------------------------------------------------------'''


if __name__ == '__main__':
    unittest.main()
