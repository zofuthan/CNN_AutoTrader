# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:26:32 2018

@author: yewei
"""

import tushare as ts
from datetime import date
import pandas as pd

defaultStartDate = '2007-01-01'
defaultEndDate = str(date.today())

#INDEX_LIST = ['000001', '000002', '000003', '000004', '000005', '000006', '000007', '000008', '000009', '000010', '000011', '000012', '000013', '000015', '000016', '000017', '000018', '000019', '000020', '000021', '000022', '000025', '000026', '000027', '000028', '000029', '000030', '000031', '000032', '000033', '000034', '000035', '000036', '000037', '000038', '000039', '000040', '000041', '000042', '000043', '000044', '000045', '000046', '000047', '000048', '000049', '000050', '000051', '000052', '000053', '000054', '000055', '000056', '000057', '000058', '000059', '000060', '000061', '000062', '000063', '000064', '000065', '000066', '000067', '000068', '000069', '000070', '000071', '000072', '000073', '000074', '000075', '000076', '000077', '000078', '000079', '000090', '000091', '000092', '000093', '000094', '000095', '000096', '000097', '000098', '000099', '000100', '000101', '000102', '000103', '000104', '000105', '000106', '000107', '000108', '000109', '000110', '000111', '000112', '000113', '000114', '000115', '000116', '000117', '000118', '000119', '000120', '000121', '000122', '000123', '000125', '000126', '000128', '000129', '000130', '000131', '000132', '000133', '000134', '000135', '000136', '000137', '000138', '000139', '000141', '000142', '000145', '000146', '000147', '000148', '000149', '000150', '000151', '000152', '000153', '000155', '000158', '000159', '000160', '000161', '000162', '000171', '000188', '000300', '000801', '000802', '000803', '000804', '000805', '000806', '000807', '000808', '000809', '000810', '000811', '000812', '000813', '000814', '000815', '000816', '000817', '000818', '000819', '000820', '000821', '000822', '000823', '000824', '000825', '000826', '000827', '000828', '000829', '000830', '000831', '000832', '000833', '000838', '000839', '000840', '000841', '000842', '000843', '000844', '000846', '000847', '000849', '000850', '000851', '000852', '000853', '000854', '000855', '000856', '000857', '000858', '000891', '000901', '000902', '000903', '000904', '000905', '000906', '000907', '000908', '000909', '000910', '000911', '000912', '000913', '000914', '000915', '000916', '000917', '000918', '000919', '000920', '000921', '000922', '000923', '000925', '000926', '000927', '000928', '000929', '000930', '000931', '000932', '000933', '000934', '000935', '000936', '000937', '000938', '000939', '000940', '000941', '000942', '000943', '000944', '000945', '000946', '000947', '000948', '000949', '000950', '000951', '000952', '000953', '000954', '000955', '000956', '000957', '000958', '000959', '000960', '000961', '000962', '000963', '000964', '000965', '000966', '000967', '000968', '000969', '000970', '000971', '000972', '000973', '000974', '000975', '000976', '000977', '000978', '000979', '000980', '000981', '000982', '000983', '000984', '000985', '000986', '000987', '000988', '000989', '000990', '000991', '000992', '000993', '000994', '000995', '000996', '000997', '000998', '000999', '399001', '399002', '399003', '399004', '399005', '399006', '399007', '399008', '399009', '399010', '399011', '399012', '399013', '399015', '399016', '399017', '399018', '399100', '399101', '399102', '399103', '399106', '399107', '399108', '399231', '399232', '399233', '399234', '399235', '399236', '399237', '399238', '399239', '399240', '399241', '399242', '399243', '399244', '399248', '399249', '399298', '399299', '399300', '399301', '399302', '399303', '399305', '399306', '399307', '399310', '399311', '399312', '399313', '399314', '399315', '399316', '399317', '399318', '399319', '399320', '399321', '399322', '399324', '399326', '399328', '399330', '399332', '399333', '399335', '399337', '399339', '399341', '399344', '399346', '399348', '399350', '399351', '399352', '399353', '399354', '399355', '399356', '399357', '399358', '399359', '399360', '399361', '399362', '399363', '399364', '399365', '399366', '399367', '399368', '399369', '399370', '399371', '399372', '399373', '399374', '399375', '399376', '399377', '399378', '399379', '399380', '399381', '399382', '399383', '399384', '399385', '399386', '399387', '399388', '399389', '399390', '399391', '399392', '399393', '399394', '399395', '399396', '399397', '399398', '399399', '399400', '399401', '399402', '399403', '399404', '399405', '399406', '399407', '399408', '399409', '399410', '399411', '399412', '399413', '399415', '399416', '399417', '399418', '399419', '399420', '399423', '399427', '399428', '399429', '399431', '399432', '399433', '399434', '399435', '399436', '399437', '399438', '399439', '399440', '399441', '399481', '399550', '399551', '399552', '399553', '399554', '399555', '399556', '399557', '399602', '399604', '399606', '399608', '399610', '399611', '399612', '399613', '399614', '399615', '399616', '399617', '399618', '399619', '399620', '399621', '399622', '399623', '399624', '399625', '399626', '399627', '399628', '399629', '399630', '399631', '399632', '399633', '399634', '399635', '399636', '399637', '399638', '399639', '399640', '399641', '399642', '399643', '399644', '399645', '399646', '399647', '399648', '399649', '399650', '399651', '399652', '399653', '399654', '399655', '399656', '399657', '399658', '399659', '399660', '399661', '399662', '399663', '399664', '399665', '399666', '399667', '399668', '399669', '399670', '399671', '399672', '399673', '399674', '399675', '399676', '399677', '399678', '399679', '399680', '399681', '399682', '399683', '399684', '399685', '399686', '399687', '399688', '399689', '399690', '399691', '399692', '399693', '399694', '399695', '399696', '399697', '399698', '399699', '399701', '399702', '399703', '399704', '399705', '399706', '399707', '399802', '399803', '399804', '399805', '399806', '399807', '399808', '399809', '399810', '399811', '399812', '399813', '399814', '399817', '399901', '399902', '399903', '399904', '399905', '399906', '399907', '399908', '399909', '399910', '399911', '399912', '399913', '399914', '399915', '399916', '399917', '399918', '399919', '399920', '399922', '399923', '399925', '399926', '399927', '399928', '399929', '399930', '399931', '399932', '399933', '399934', '399935', '399936', '399937', '399938', '399939', '399940', '399941', '399942', '399943', '399944', '399945', '399946', '399947', '399948', '399949', '399950', '399951', '399952', '399953', '399954', '399955', '399956', '399957', '399958', '399959', '399960', '399961', '399962', '399963', '399964', '399965', '399966', '399967', '399968', '399969', '399970', '399971', '399972', '399973', '399974', '399975', '399976', '399977', '399978', '399979', '399980', '399981', '399982', '399983', '399984', '399985', '399986', '399987', '399989', '399990', '399991', '399992', '399993', '399994', '399995', '399996', '399997', '399998']
#INDEX_LIST = ['000001', '000009', '000010', '000011', '000015', '000016', '000300', '000852', '000902', '000903', '000904', '000905', '000906', '000907', '399001', '399005', '399006', '399678']
INDEX_LIST = ['000300']
#INDEX_LIST = ['399678']

#code = input("Input Index Code : ")
startDate = input("Input Start Date (%s) : " %defaultStartDate)
endDate = input("Input End Date (%s) : " %defaultEndDate)

startIdx1 = input("Input Start Num (0): ")
if startIdx1=='':
    startIdx = 0
else:
    startIdx = int(startIdx1)

currIdx = 0
for code in INDEX_LIST:
    
    print('Curr Processing Index : %d' %currIdx)
    
    if currIdx < startIdx:
        currIdx+=1
        continue
    
    currIdx+=1
    try:
       
        if startDate=="":
            startDate = defaultStartDate
        if endDate=="":
            endDate = defaultEndDate
            
        outputFileName = 'DataDownload/Data_%s_(%s)_(%s).csv' %(code, startDate, endDate)
        print('Data Download to : %s' %outputFileName)
        
        df = ts.get_k_data(code, index=True, start=str(startDate), end=str(endDate))
        del df['date']
        del df['code']
        
        rows = len(df)
        
        print('Data has %d Rows ... ' %rows)
        
        #data process
        TRAIN_DAYS = 64
        PERDICT_DAYS = 1
        RANGE_END = rows-TRAIN_DAYS-(PERDICT_DAYS-1)
        
        if rows<=TRAIN_DAYS+(PERDICT_DAYS-1):
            continue
            
        table = pd.DataFrame()
        for i in range(0, TRAIN_DAYS):
            colname1 = 'O%d' %i
            colname2 = 'C%d' %i
            colname3 = 'H%d' %i
            colname4 = 'L%d' %i
            colname5 = 'V%d' %i
            table[colname1] = None
            table[colname2] = None
            table[colname3] = None
            table[colname4] = None
            table[colname5] = None
        table['UP'] = None
        table['DOWN'] = None
        
        for i in range(0, RANGE_END):
            growth = float(df['close'][(i+TRAIN_DAYS+(PERDICT_DAYS-1))]) / float(df['low'][(i+TRAIN_DAYS)-1]) - 1
            kdatapart = df[i:i+TRAIN_DAYS]
            kdatapart = kdatapart.reset_index(drop=True)
            lowlist = []
            volumelist = []
            feeddata = []
            for j in range(0, len(kdatapart)):
                lowlist.append(float(kdatapart['low'][j]))
                volumelist.append(float(kdatapart['volume'][j]))
            low_min = min(lowlist)
            low_max = max(lowlist)
            volume_min = min(volumelist)
            volume_max = max(volumelist)
            for j in range(0, len(kdatapart)):
                fopen = float(kdatapart['open'][j])
                fclose = float(kdatapart['close'][j])
                fhigh = float(kdatapart['high'][j])
                flow = float(kdatapart['low'][j])
                fvolume = float(kdatapart['volume'][j])
                unified_open = (fopen-low_min)/(low_max-low_min)
                unified_close = (fclose-low_min)/(low_max-low_min)
                unified_high = (fhigh-low_min)/(low_max-low_min)
                unified_low = (flow-low_min)/(low_max-low_min)
                unified_vol = (fvolume-volume_min)/(volume_max-volume_min)
                feeddata.append(unified_open)
                feeddata.append(unified_close)
                feeddata.append(unified_high)
                feeddata.append(unified_low)
                feeddata.append(unified_vol)
            up = 1.0
            down = 0.0
            if growth*100.0>=1.0:
                up = 1.0
                down = 0.0
            else:
                up = 0.0
                down = 1.0
            feeddata.append(up)
            feeddata.append(down)
            
            table.loc[len(table.index)] = feeddata
            
            if i%100==0:
                percent = i / float(RANGE_END) * 100.0
                print("Exporting %0.2f%% ..." %percent)
        
        print('Saving To %s ...' %outputFileName)
        
        table = table.dropna(axis=0, how='any')
        table = table.drop_duplicates()
        
        table.to_csv(path_or_buf=outputFileName, index=False, header=True)
        
        print('Data Saved ...')
        
    except:
        continue