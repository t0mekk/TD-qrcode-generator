'''
Matthew Ragan | matthewragan.com
'''

import qrcode

class Qrcode:
    # '''
	# 	This is a sample class.

	# 	This sample class has several important features that can be described here.


	# 	Notes
	# 	---------------
	# 	Your notes about the class go here
 	# '''
	def __init__(self, myOp):
		self.Myop = myOp
		self.File_name = myOp.par.Filename
		self.Save_folder = myOp.par.Savefolder
		self.Qrdata = myOp.par.Qrdata
		self.MoviefileinTOP = op("moviefilein1")
		pass

	def Make_save_path(self):
		save_path = '{}/{}.png'.format(self.Save_folder, self.File_name)
		return save_path

	def Get_qr_data(self):
		return self.Qrdata.eval()
		
	def Load_result(self, filePath):
		self.MoviefileinTOP.par.file = filePath
		self.MoviefileinTOP.par.reloadpulse.pulse()
		pass

	def Make_qr_code(self):
		qr_img = qrcode.make(self.Get_qr_data())
		save_path = self.Make_save_path()
		qr_img.save(save_path)
		self.Load_result(save_path)
		pass
