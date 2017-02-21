# -*- coding: utf-8 -*-
__author__ = 'Jerry'

'''
excel report
'''
from Emachine import *
from log_s import *
import xlsxwriter
import os
import sys
sys.coinit_flags = 0
import win32com.client
import global_argu
import pythoncom
import configparser


class report(object):

	def __init__(self, distance, Tx, Rx, RSSI, LinkRate, STA_RSSI, Time, dot11_2, dot11_5):
		self.distance = distance
		self.Tx = Tx
		self.Rx = Rx
		self.RSSI = RSSI
		self.LinkRate = LinkRate
		self.STA_RSSI = STA_RSSI
		self.Time = Time
		self.dot11_2 = dot11_2
		self.dot11_5 = dot11_5

	def create_report(self, k):
		if k == 9:
			directory = os.path.exists('D:\Python_project\Pro\TP_8\iperflog')
			if directory is True:
				os.chdir('D:\Python_project\Pro\TP_8\iperflog')
				workbook = xlsxwriter.Workbook('TP_Tmp_Report.xlsx')
				worksheet = workbook.add_worksheet()
				# argument
				title = [u'Distance(m)', u'Encription', u'Radio', u'Chn', u'Angle', u'TX', u'RX', u'RSSI', u'LinkRate', u'STA_RSSI', u'RunTime']
				columns_8 = [u'0°', u'45°', u'90°', u'135°', u'180°', u'225°', u'270°', u'315°']
				columns_4 = [u'0°', u'90°',  u'180°', u'270°']
				columns_time_8 = ['%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time]
				columns_time_4 = ['%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time, '%ss' % self.Time]
				columns_null_8 = [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'']
				columns_null_4 = [u'', u'', u'', u'', u'', u'', u'', u'']
				columns_null_4_2 = [u'', u'', u'', u'']
				# title
				format_title = workbook.add_format()
				format_title.set_border(1)
				format_title.set_bg_color('#EEC591')
				format_title.set_bold(1)
				format_title.set_font_color('#8B2500')
				worksheet.write_row('A1', title, format_title)
				# column distance 10m & 50m
				format_m = workbook.add_format()
				format_m.set_bg_color('#EEC591')
				format_m.set_border(1)
				format_m.set_font_color('#8B2500')
				format_m.set_align('center')
				format_m.set_align('vcenter')
				format_m.set_bold(1)
				# date format
				format_m_date = workbook.add_format()
				format_m_date.set_bold(1)
				format_m_date.set_border(1)
				format_m_date.set_bg_color('#AEEEEE')
				format_m_date.set_font_color('#050505')
				format_m_date.set_align('center')
				format_m_date.set_align('vcenter')
				# insert date
				if len(self.distance) == 1:
					if global_argu.degree == '8':
						if len(global_argu.Report_band) == 1:
							if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
								worksheet.merge_range('A2:A9', self.distance[0], format_m)
								worksheet.merge_range('B2:B9', 'open', format_m)
								worksheet.merge_range('C2:C9', global_argu.Report_band[0], format_m)
								if global_argu.Report_band[0] == global_argu.dot11_2dg:
									worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
								elif global_argu.Report_band[0] == global_argu.dot11_5dg:
									worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
								else:
									LogMsg(log.logger.error, 'Report_band is ERROR!')
								worksheet.write_column('E2:E9', columns_8, format_m)
								# time
								worksheet.write_column('K2:K9', columns_time_8, format_m_date)
								worksheet.write_column('F2:F9', columns_null_4, format_m_date)
								worksheet.write_column('G2:G9', columns_null_4, format_m_date)
								worksheet.write_column('H2:H9', columns_null_4, format_m_date)
								worksheet.write_column('I2:I9', columns_null_4, format_m_date)
								worksheet.write_column('J2:J9', columns_null_4, format_m_date)
							else:
								LogMsg(log.logger.error, 'NO Band')
						elif len(global_argu.Report_band) == 2:
							worksheet.merge_range('A2:A17', self.distance[0], format_m)
							worksheet.merge_range('B2:B17', 'open', format_m)
							worksheet.merge_range('C2:C9', '2.4G', format_m)
							worksheet.merge_range('C10:C17', '5G', format_m)
							worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D10:D17', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E2:E9', columns_8, format_m)
							worksheet.write_column('E10:E17', columns_8, format_m)
							# time
							worksheet.write_column('K2:K9', columns_time_8, format_m_date)
							worksheet.write_column('K10:K17', columns_time_8, format_m_date)
							worksheet.write_column('F2:F17', columns_null_8, format_m_date)
							worksheet.write_column('G2:G17', columns_null_8, format_m_date)
							worksheet.write_column('H2:H17', columns_null_8, format_m_date)
							worksheet.write_column('I2:I17', columns_null_8, format_m_date)
							worksheet.write_column('J2:J17', columns_null_8, format_m_date)
						else:
							LogMsg(log.logger.error, 'NO Band')

					elif global_argu.degree == '4':
						if len(global_argu.Report_band) == 1:
							if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
								worksheet.merge_range('A2:A5', self.distance[0], format_m)
								worksheet.merge_range('B2:B5', 'open', format_m)
								worksheet.merge_range('C2:C5', global_argu.Report_band[0], format_m)
								if global_argu.Report_band[0] == global_argu.dot11_2dg:
									worksheet.merge_range('D2:D5', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
								elif global_argu.Report_band[0] == global_argu.dot11_5dg:
									worksheet.merge_range('D2:D5', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
								else:
									LogMsg(log.logger.error, 'Report_band is ERROR')
								worksheet.write_column('E2:E5', columns_4, format_m)
								# time
								worksheet.write_column('K2:K5', columns_time_4, format_m_date)
								worksheet.write_column('F2:F5', columns_null_4_2, format_m_date)
								worksheet.write_column('G2:G5', columns_null_4_2, format_m_date)
								worksheet.write_column('H2:H5', columns_null_4_2, format_m_date)
								worksheet.write_column('I2:I5', columns_null_4_2, format_m_date)
								worksheet.write_column('J2:J5', columns_null_4_2, format_m_date)
							else:
								LogMsg(log.logger.error, 'NO BAND')
						elif len(global_argu.Report_band) == 2:
							worksheet.merge_range('A2:A9', self.distance[0], format_m)
							worksheet.merge_range('B2:B9', 'open', format_m)
							worksheet.merge_range('C2:C5', '2.4G', format_m)
							worksheet.merge_range('C6:C9', '5G', format_m)
							worksheet.merge_range('D2:D5', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D6:D9', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E2:E5', columns_4, format_m)
							worksheet.write_column('E6:E9', columns_4, format_m)
							# time
							worksheet.write_column('K2:K5', columns_time_4, format_m_date)
							worksheet.write_column('K6:K9', columns_time_4, format_m_date)
							worksheet.write_column('F2:F9', columns_null_4, format_m_date)
							worksheet.write_column('G2:G9', columns_null_4, format_m_date)
							worksheet.write_column('H2:H9', columns_null_4, format_m_date)
							worksheet.write_column('I2:I9', columns_null_4, format_m_date)
							worksheet.write_column('J2:J9', columns_null_4, format_m_date)
						else:
							LogMsg(log.logger.error, 'NO BAND')
					else:
						LogMsg(log.logger.error, 'NO Degree')
				elif len(self.distance) == 2:
					if global_argu.degree == '8':
						if len(global_argu.Report_band) == 1:
							if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
								worksheet.merge_range('A2:A9', self.distance[0], format_m)
								worksheet.merge_range('A10:A17', self.distance[1], format_m)
								worksheet.merge_range('B2:B17', 'open', format_m)
								worksheet.merge_range('C2:C17', global_argu.Report_band[0], format_m)
								if global_argu.Report_band[0] == global_argu.dot11_2dg:
									worksheet.merge_range('D2:D17', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
								elif global_argu.Report_band[0] == global_argu.dot11_5dg:
									worksheet.merge_range('D2:D17', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
								else:
									LogMsg(log.logger.error, 'Report_band is ERROR')
								worksheet.write_column('E2:E9', columns_8, format_m)
								worksheet.write_column('E10:E17', columns_8, format_m)
								# time
								worksheet.write_column('K2:K9', columns_time_8, format_m_date)
								worksheet.write_column('K10:K17', columns_time_8, format_m_date)
								worksheet.write_column('F2:F17', columns_null_8, format_m_date)
								worksheet.write_column('G2:G17', columns_null_8, format_m_date)
								worksheet.write_column('H2:H17', columns_null_8, format_m_date)
								worksheet.write_column('I2:I17', columns_null_8, format_m_date)
								worksheet.write_column('J2:J17', columns_null_8, format_m_date)
							else:
								LogMsg(log.logger.error, 'NO BAND')
						elif len(global_argu.Report_band) == 2:
							worksheet.merge_range('A2:A17', self.distance[0], format_m)
							worksheet.merge_range('B2:B17', 'open', format_m)
							worksheet.merge_range('C2:C9', '2.4G', format_m)
							worksheet.merge_range('C10:C17', '5G', format_m)
							worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D10:D17', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E2:E9', columns_8, format_m)
							worksheet.write_column('E10:E17', columns_8, format_m)
							# time
							worksheet.write_column('K2:K9', columns_time_8, format_m_date)
							worksheet.write_column('K10:K17', columns_time_8, format_m_date)
							worksheet.write_column('F2:F17', columns_null_8, format_m_date)
							worksheet.write_column('G2:G17', columns_null_8, format_m_date)
							worksheet.write_column('H2:H17', columns_null_8, format_m_date)
							worksheet.write_column('I2:I17', columns_null_8, format_m_date)
							worksheet.write_column('J2:J17', columns_null_8, format_m_date)
							worksheet.merge_range('A18:A33', self.distance[1], format_m)
							worksheet.merge_range('B18:B33', 'open', format_m)
							worksheet.merge_range('C18:C25', '2.4G', format_m)
							worksheet.merge_range('C26:C33', '5G', format_m)
							worksheet.merge_range('D18:D25', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D26:D33', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E18:E25', columns_8, format_m)
							worksheet.write_column('E26:E33', columns_8, format_m)
							# time
							worksheet.write_column('K18:K25', columns_time_8, format_m_date)
							worksheet.write_column('K26:K33', columns_time_8, format_m_date)
							worksheet.write_column('F18:F33', columns_null_8, format_m_date)
							worksheet.write_column('G18:G33', columns_null_8, format_m_date)
							worksheet.write_column('H18:H33', columns_null_8, format_m_date)
							worksheet.write_column('I18:I33', columns_null_8, format_m_date)
							worksheet.write_column('J18:J33', columns_null_8, format_m_date)
						else:
							LogMsg(log.logger.error, 'NO BAND')
					elif global_argu.degree == '4':
						if len(global_argu.Report_band) == 1:
							if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
								worksheet.merge_range('A2:A5', self.distance[0], format_m)
								worksheet.merge_range('A6:A9', self.distance[1], format_m)
								worksheet.merge_range('B2:B9', 'open', format_m)
								worksheet.merge_range('C2:C9', global_argu.Report_band[0], format_m)
								if global_argu.Report_band[0] == global_argu.dot11_2dg:
									worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
								elif global_argu.Report_band[0] == global_argu.dot11_5dg:
									worksheet.merge_range('D2:D9', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
								else:
									LogMsg(log.logger.error, 'Report_band is ERROR')
								worksheet.write_column('E2:E5', columns_4, format_m)
								worksheet.write_column('E6:E9', columns_4, format_m)
								# time
								worksheet.write_column('K2:K5', columns_time_4, format_m_date)
								worksheet.write_column('K6:K9', columns_time_4, format_m_date)
								worksheet.write_column('F2:F9', columns_null_4, format_m_date)
								worksheet.write_column('G2:G9', columns_null_4, format_m_date)
								worksheet.write_column('H2:H9', columns_null_4, format_m_date)
								worksheet.write_column('I2:I9', columns_null_4, format_m_date)
								worksheet.write_column('J2:J9', columns_null_4, format_m_date)
							else:
								LogMsg(log.logger.error, 'NO BAND')
						elif len(global_argu.Report_band) == 2:
							worksheet.merge_range('A2:A9', self.distance[0], format_m)
							worksheet.merge_range('B2:B9', 'open', format_m)
							worksheet.merge_range('C2:C5', '2.4G', format_m)
							worksheet.merge_range('C6:C9', '5G', format_m)
							worksheet.merge_range('D2:D5', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D6:D9', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E2:E5', columns_4, format_m)
							worksheet.write_column('E6:E9', columns_4, format_m)
							# time
							worksheet.write_column('K2:K5', columns_time_4, format_m_date)
							worksheet.write_column('K6:K9', columns_time_4, format_m_date)
							worksheet.write_column('F2:F9', columns_null_4, format_m_date)
							worksheet.write_column('G2:G9', columns_null_4, format_m_date)
							worksheet.write_column('H2:H9', columns_null_4, format_m_date)
							worksheet.write_column('I2:I9', columns_null_4, format_m_date)
							worksheet.write_column('J2:J9', columns_null_4, format_m_date)
							worksheet.merge_range('A10:A17', self.distance[1], format_m)
							worksheet.merge_range('B10:B17', 'open', format_m)
							worksheet.merge_range('C10:C13', '2.4G', format_m)
							worksheet.merge_range('C14:C17', '5G', format_m)
							worksheet.merge_range('D10:D13', '%s_%s'%(global_argu.AP_channel_2,global_argu.AP_bd_2), format_m)
							worksheet.merge_range('D14:D17', '%s_%s'%(global_argu.AP_channel_5,global_argu.AP_bd_5), format_m)
							worksheet.write_column('E10:E13', columns_4, format_m)
							worksheet.write_column('E14:E17', columns_4, format_m)
							# time
							worksheet.write_column('K10:K13', columns_time_4, format_m_date)
							worksheet.write_column('K14:K17', columns_time_4, format_m_date)
							worksheet.write_column('F10:F17', columns_null_4, format_m_date)
							worksheet.write_column('G10:G17', columns_null_4, format_m_date)
							worksheet.write_column('H10:H17', columns_null_4, format_m_date)
							worksheet.write_column('I10:I17', columns_null_4, format_m_date)
							worksheet.write_column('J10:J17', columns_null_4, format_m_date)
						else:
							LogMsg(log.logger.error, 'NO BAND')
					else:
						LogMsg(log.logger.error, 'NO Degree')
				else:
					LogMsg(log.logger.error, 'NO Distance')
				workbook.close()
			else:
				LogMsg(log.logger.error, 'NO Directory')
				os.system('TASKKILL /F /IM EXCEL.exe')
		else:
			LogMsg(log.logger.error, 'Can''t Create Report!')

	def degree_report(self, k):
		directory = os.path.exists('D:\Python_project\Pro\TP_8\iperflog')
		if directory is True:
			os.chdir('D:\Python_project\Pro\TP_8\iperflog')
			files = os.path.isfile('TP_Tmp_Report.xlsx')
			if files is True:
				pythoncom.CoInitialize()
				winapp = win32com.client.DispatchEx('Excel.Application')
				#winapp.Visible = 1
				winbook = winapp.Workbooks.Open('D:\Python_project\Pro\TP_8\iperflog\TP_Tmp_Report.xlsx')
				winsheet = winbook.ActiveSheet
				# argument_0
				tx_location_1 = 'F%d' % (int(k)+2)
				rx_location_1 = 'G%d' % (int(k)+2)
				rssi_location_1 = 'H%d' % (int(k)+2)
				linkrate_location_1 = 'I%d' % (int(k)+2)
				sta_rssi_location_1 = 'J%d' % (int(k)+2)
				# argument_1
				tx_location_1_8 = 'F%d' % (int(k)+10)
				rx_location_1_8 = 'G%d' % (int(k)+10)
				rssi_location_1_8 = 'H%d' % (int(k)+10)
				linkrate_location_1_8 = 'I%d' % (int(k)+10)
				sta_rssi_location_1_8 = 'J%d' % (int(k)+10)
				tx_location_1_4 = 'F%d' % (int(k)+6)
				rx_location_1_4 = 'G%d' % (int(k)+6)
				rssi_location_1_4 = 'H%d' % (int(k)+6)
				linkrate_location_1_4 = 'I%d' % (int(k)+6)
				sta_rssi_location_1_4 = 'J%d' % (int(k)+6)
				# argument_2
				tx_location_2_8 = 'F%d' % (int(k)+18)
				rx_location_2_8 = 'G%d' % (int(k)+18)
				rssi_location_2_8 = 'H%d' % (int(k)+18)
				linkrate_location_2_8 = 'I%d' % (int(k)+18)
				sta_rssi_location_2_8 = 'J%d' % (int(k)+18)
				tx_location_2_5_8 = 'F%d' % (int(k)+26)
				rx_location_2_5_8 = 'G%d' % (int(k)+26)
				rssi_location_2_5_8 = 'H%d' % (int(k)+26)
				linkrate_location_2_5_8 = 'I%d' % (int(k)+26)
				sta_rssi_location_2_5_8 = 'J%d' % (int(k)+26)
				tx_location_2_4 = 'F%d' % (int(k)+10)
				rx_location_2_4 = 'G%d' % (int(k)+10)
				tx_location_2_5_4 = 'F%d' % (int(k)+14)
				rx_location_2_5_4 = 'G%d' % (int(k)+14)
				rssi_location_2_4 = 'H%d' % (int(k)+10)
				linkrate_location_2_4 = 'I%d' % (int(k)+10)
				rssi_location_2_5_4 = 'H%d' % (int(k)+14)
				linkrate_location_2_5_4 = 'I%d' % (int(k)+14)
				sta_rssi_location_2_4 = 'J%d' % (int(k)+10)
				sta_rssi_location_2_5_4 = 'J%d' % (int(k)+14)
				# insert date
				config = configparser.ConfigParser()
				config.read('D:\Python_project\Pro\TP_8\config.ini')
				dis_flag_D = config.get('other_config', 'dis_flag')
				if len(self.distance) == 1:
					if self.distance[0] == global_argu.check3 or self.distance[0] == global_argu.check4:
						if global_argu.degree == '8' or global_argu.degree == '4':
							if len(global_argu.Report_band) == 1:
								if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
									if self.Tx == None and self.Rx ==None and self.STA_RSSI ==None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(rssi_location_1).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1).FormulaR1C1 = self.LinkRate
									elif self.STA_RSSI != None and(self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(sta_rssi_location_1).FormulaR1C1 = self.STA_RSSI
									elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(tx_location_1).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1).FormulaR1C1 = self.Rx
										emachine = Emachine()
										if global_argu.degree == '8':
											emachine.degree_45(k)
										elif global_argu.degree =='4':
											emachine.degree_90(k)
										else:
											LogMsg(log.logger.error, 'NO degree_machine!')
									else:
										LogMsg(log.logger.error, 'NO Data_D1_B1!')
								else:
									LogMsg(log.logger.error, 'NO BAND')
								winbook.Save()
								winbook.Close(SaveChanges=0)

							elif len(global_argu.Report_band) == 2:
								if self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(rssi_location_1).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree!')
								elif self.STA_RSSI != None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(sta_rssi_location_1).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(rssi_location_1_8).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1_8).FormulaR1C1 = self.LinkRate
									elif global_argu.degree == '4':
										winsheet.Range(rssi_location_1_4).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1_4).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.STA_RSSI != None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(sta_rssi_location_1_8).FormulaR1C1 = self.STA_RSSI
									elif global_argu.degree == '4':
										winsheet.Range(sta_rssi_location_1_4).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(tx_location_1).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1).FormulaR1C1 = self.Rx
										emachine = Emachine()
										if global_argu.degree == '8':
											emachine.degree_45(k)
										elif global_argu.degree == '4':
											emachine.degree_90(k)
										else:
											LogMsg(log.logger.error, 'NO degree_machine!')
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(tx_location_1_8).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1_8).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_45(k)
									elif global_argu.degree == '4':
										winsheet.Range(tx_location_1_4).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1_4).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_90(k)
									else:
										LogMsg(log.logger.error, 'NO Degree')
								else:
									LogMsg(log.logger.error, 'NO DATA_D1_B2')
								winbook.Save()
								winbook.Close(SaveChanges=0)
							else:
								LogMsg(log.logger.error, 'NO BAND')
						else:
							LogMsg(log.logger.error, 'NO Degree')
					else:
						LogMsg(log.logger.error, "The distance you choose != report's distance!")

				elif len(self.distance) == 2:
					if global_argu.degree == '8' or global_argu.degree == '4':
						if len(global_argu.Report_band) == 1:
							if global_argu.Report_band[0] == global_argu.dot11_2dg or global_argu.Report_band[0] == global_argu.dot11_5dg:
								if self.distance[0] == global_argu.check3 and dis_flag_D == '1':
									if self.Tx == None and self.Rx ==None and self.STA_RSSI == None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(rssi_location_1).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1).FormulaR1C1 = self.LinkRate
									elif self.STA_RSSI != None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(sta_rssi_location_1).FormulaR1C1 = self.STA_RSSI
									elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										winsheet.Range(tx_location_1).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1).FormulaR1C1 = self.Rx
										emachine = Emachine()
										if global_argu.degree == '8':
											emachine.degree_45(k)
										elif global_argu.degree == '4':
											emachine.degree_90(k)
										else:
											LogMsg(log.logger.error, 'NO degree_machine')
									else:
										LogMsg(log.logger.error, 'NO DATA_D2_B1!')

									'''
									Copy Data!
									'''
									file_data = os.path.isfile('D:\Python_project\Pro\TP_8\data.txt')
									if file_data is True:
										pass
									else:
										os.chdir('D:\Python_project\Pro\TP_8')
										f = open('data.txt', 'w')
										f.close()
									startcol = 'F'
									endcol = 'J'
									f = open('D:\Python_project\Pro\TP_8\data.txt', 'a+')
									tupled_2 = winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value
									tuple_list_2 = [line+','for line in tuple(map(str, tupled_2))]
									f.writelines(tuple_list_2)
									f.write('\n')
									f.close()
									winbook.Save()
									winbook.Close(SaveChanges=0)

								elif self.distance[1] == global_argu.check4 and dis_flag_D == '2':
									'''
									Write Data!
									'''
									startcol = 'F'
									endcol = 'J'
									f = open('D:\Python_project\Pro\TP_8\data.txt', 'r+')
									data = f.readlines()
									if global_argu.degree == '8':
										winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value = tuple(data[(int(k)*3)+2].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
									elif global_argu.degree == '4':
										winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value = tuple(data[(int(k)*3)+2].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
									else:
										LogMsg(log.logger.error, 'NO Degree!')
									f.close()
									'''
									New distance Data!
									'''
									if self.Tx == None and self.Rx ==None and self.STA_RSSI == None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										if global_argu.degree == '8':
											winsheet.Range(rssi_location_1_8).FormulaR1C1 = self.RSSI
											winsheet.Range(linkrate_location_1_8).FormulaR1C1 = self.LinkRate
										elif global_argu.degree == '4':
											winsheet.Range(rssi_location_1_4).FormulaR1C1 = self.RSSI
											winsheet.Range(linkrate_location_1_4).FormulaR1C1 = self.LinkRate
										else:
											LogMsg(log.logger.error, 'NO Degree')
									elif self.STA_RSSI != None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										if global_argu.degree == '8':
											winsheet.Range(sta_rssi_location_1_8).FormulaR1C1 = self.STA_RSSI
										elif global_argu.degree == '4':
											winsheet.Range(sta_rssi_location_1_4).FormulaR1C1 =self.STA_RSSI
										else:
											LogMsg(log.logger.error, 'NO STA_RSSI')
									elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and (self.dot11_2 == '2.4G' or self.dot11_5 == '5G'):
										if global_argu.degree == '8':
											winsheet.Range(tx_location_1_8).FormulaR1C1 = self.Tx
											winsheet.Range(rx_location_1_8).FormulaR1C1 = self.Rx
											emachine = Emachine()
											emachine.degree_45(k)
										elif global_argu.degree == '4':
											winsheet.Range(tx_location_1_4).FormulaR1C1 = self.Tx
											winsheet.Range(rx_location_1_4).FormulaR1C1 = self.Rx
											emachine = Emachine()
											emachine.degree_90(k)
										else:
											LogMsg(log.logger.error, 'NO Degree')
									else:
										LogMsg(log.logger.error, 'NO DATA_1')
									winbook.Save()
									winbook.Close(SaveChanges=0)
								else:
									LogMsg(log.logger.error, 'NO Distance!')

						elif len(global_argu.Report_band) == 2:
							if self.distance[0] == global_argu.check3 and dis_flag_D == '1':
								if self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(rssi_location_1).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(rssi_location_1_8).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1_8).FormulaR1C1 = self.LinkRate
									elif global_argu.degree == '4':
										winsheet.Range(rssi_location_1_4).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_1_4).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.STA_RSSI != None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(sta_rssi_location_1).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.STA_RSSI != None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(sta_rssi_location_1_8).FormulaR1C1 = self.STA_RSSI
									elif global_argu.degree == '4':
										winsheet.Range(sta_rssi_location_1_4).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8' or global_argu.degree == '4':
										winsheet.Range(tx_location_1).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1).FormulaR1C1 = self.Rx
										emachine = Emachine()
										if global_argu.degree == '8':
											emachine.degree_45(k)
										elif global_argu.degree =='4':
											emachine.degree_90(k)
										else:
											LogMsg(log.logger.error, 'NO degree_machine!')
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(tx_location_1_8).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1_8).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_45(k)
									elif global_argu.degree == '4':
										winsheet.Range(tx_location_1_4).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_1_4).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_90(k)
									else:
										LogMsg(log.logger.error, 'NO Degree')
								else:
									LogMsg(log.logger.error, 'NO DATA_D2_B2!')
								'''
								Copy Data!
								'''
								file_data = os.path.isfile('D:\Python_project\Pro\TP_8\data.txt')
								if file_data is True:
									pass
								else:
									os.chdir('D:\Python_project\Pro\TP_8')
									f = open('data.txt', 'w')
									f.close()
								startcol = 'F'
								endcol = 'J'
								f = open('D:\Python_project\Pro\TP_8\data.txt', 'a+')
								if global_argu.degree == '8':
									tupled_2 = winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value
									tupled_5 = winsheet.Range(winsheet.Cells(int(k)+10, startcol), winsheet.Cells(int(k)+10, endcol)).Value
									tuple_list_2 = [line+','for line in tuple(map(str, tupled_2))]
									tuple_list_5 = [line+','for line in tuple(map(str, tupled_5))]
									f.writelines(tuple_list_2)
									f.write('\n')
									f.writelines(tuple_list_5)
									f.write('\n')
								elif global_argu.degree == '4':
									tupled_2 = winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value
									tupled_5 = winsheet.Range(winsheet.Cells(int(k)+6, startcol), winsheet.Cells(int(k)+6, endcol)).Value
									tuple_list_2 = [line+','for line in tuple(map(str, tupled_2))]
									tuple_list_5 = [line+','for line in tuple(map(str, tupled_5))]
									f.writelines(tuple_list_2)
									f.write('\n')
									f.writelines(tuple_list_5)
									f.write('\n')
								f.close()
								winbook.Save()
								winbook.Close(SaveChanges=0)
							elif self.distance[1] == global_argu.check4 and dis_flag_D == '2':
								"""
								Write data!
								"""
								startcol = 'F'
								endcol = 'J'
								f = open('D:\Python_project\Pro\TP_8\data.txt', 'r+')
								data = f.readlines()
								if global_argu.degree == '8':
									winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value = tuple(data[(int(k)*6)+4].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
									winsheet.Range(winsheet.Cells(int(k)+10, startcol), winsheet.Cells(int(k)+10, endcol)).Value = tuple(data[(int(k)*6)+53].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
								elif global_argu.degree == '4':
									winsheet.Range(winsheet.Cells(int(k)+2, startcol), winsheet.Cells(int(k)+2, endcol)).Value = tuple(data[(int(k)*6)+4].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
									winsheet.Range(winsheet.Cells(int(k)+6, startcol), winsheet.Cells(int(k)+6, endcol)).Value = tuple(data[(int(k)*6)+29].strip('\n').strip('()')[:-1].strip('()').strip('\'').split(','))
								f.close()
								'''
								New Data
								'''
								if self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8':
										winsheet.Range(rssi_location_2_8).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_2_8).FormulaR1C1 = self.LinkRate
									elif global_argu.degree == '4':
										winsheet.Range(rssi_location_2_4).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_2_4).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.Tx == None and self.Rx ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(rssi_location_2_5_8).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_2_5_8).FormulaR1C1 = self.LinkRate
									elif global_argu.degree == '4':
										winsheet.Range(rssi_location_2_5_4).FormulaR1C1 = self.RSSI
										winsheet.Range(linkrate_location_2_5_4).FormulaR1C1 = self.LinkRate
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.STA_RSSI != None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8':
										winsheet.Range(sta_rssi_location_2_8).FormulaR1C1 = self.STA_RSSI
									elif global_argu.degree == '4':
										winsheet.Range(sta_rssi_location_2_4).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.STA_RSSI != None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(sta_rssi_location_2_5_8).FormulaR1C1 = self.STA_RSSI
									elif global_argu.degree =='4':
										winsheet.Range(sta_rssi_location_2_5_4).FormulaR1C1 = self.STA_RSSI
									else:
										LogMsg(log.logger.error, 'NO STA_RSSI')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI ==None and self.dot11_2 == '2.4G':
									if global_argu.degree == '8':
										winsheet.Range(tx_location_2_8).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_2_8).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_45(k)
									elif global_argu.degree == '4':
										winsheet.Range(tx_location_2_4).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_2_4).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_90(k)
									else:
										LogMsg(log.logger.error, 'NO Degree')
								elif self.RSSI == None and self.LinkRate ==None and self.STA_RSSI == None and self.dot11_5 == '5G':
									if global_argu.degree == '8':
										winsheet.Range(tx_location_2_5_8).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_2_5_8).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_45(k)
									elif global_argu.degree == '4':
										winsheet.Range(tx_location_2_5_4).FormulaR1C1 = self.Tx
										winsheet.Range(rx_location_2_5_4).FormulaR1C1 = self.Rx
										emachine = Emachine()
										emachine.degree_90(k)
								else:
									LogMsg(log.logger.error, 'NO DATA_2!')
								winbook.Save()
								winbook.Close(SaveChanges=0)
							else:
								LogMsg(log.logger.error, "The distance you choose != report's distance2!")
								winbook.Close(SaveChanges=0)
						else:
							LogMsg(log.logger.error, 'NO BAND')
							winbook.Close(SaveChanges=0)
					else:
						LogMsg(log.logger.error, 'NO Degree!')
						winbook.Close(SaveChanges=0)
				else:
					LogMsg(log.logger.error, 'NO Distance!')
				pythoncom.CoUninitialize()
			else:
				LogMsg(log.logger.error, 'NO FILE')
				os.system('TASKKILL /F /IM EXCEL.exe')
		else:
			LogMsg(log.logger.error, 'NO Directory')
			os.system('TASKKILL /F /IM EXCEL.exe')

if __name__ == '__main__':
	# Get from gui
	listd = []
	Txd = '100'
	Rxd = '200'
	Rssi = '60'
	Linkrate = '144'
	timed = '90'
	q = '0'
	dot11_2g = '2.4G'
	dot11_5g = '5G'
	while True:
		raw = input('Please input the distance:')
		if raw == '':
			break
		else:
			listd.append(raw)
	r = report(listd, Txd, Rxd, Rssi, Linkrate, timed, dot11_2g, dot11_5g)
	r.create_report(q)
	r.degree_report(q)

