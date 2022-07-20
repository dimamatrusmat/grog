from docx2pdf import convert
import pikepdf
import os


dir = os.path.abspath(os.curdir)
indir = dir + '\\input\\'
outdir =  dir + '\\output\\'

def del_pages(pdf, arr, num_pages=16):
	max = arr[1]
	min = arr[0] - 1

	del pdf.pages[max:num_pages]
	del pdf.pages[0:min]

	return pdf

def tackword(arr):
	out = []

	for file in arr:
		if '.docx' in file:
			out.append(file)

	return out

def doc_crushing(doc_path, arr, outpdf):
	with pikepdf.open(doc_path) as pdf:
		num_pages = len(pdf.pages)
		#Удаляем страницы из pdf
		del_pages(pdf, arr, num_pages)

		pdf.save(outdir+outpdf)
	   

def main():
	input_files = tackword(next(os.walk('.\\input'))[2])

	# for file in input_files:
	#     convert(indir+file)

	input_pds = next(os.walk('.\\input'))[2]

	doc = ''
	rec = ''

	outs = []

	for file in input_pds:
		if '.pdf' in file:
			if 'Договор' in file:
				doc = file
			elif 'Реквизиты' in file:
				rec = file
			else:
				outs.append(file)

	# Открываем договор pdf, если он есть
	if doc != '':			
		doc_path = indir + doc

		doc_crushing(doc_path, [1,2], 'Титульный лист.pdf')
		doc_crushing(doc_path, [3,4], 'Экзаменационный лист с фото.pdf')
		doc_crushing(doc_path, [5,6], 'Заявление на поступление.pdf')
		doc_crushing(doc_path, [7,7], 'Согласие на зачисление.pdf')
		doc_crushing(doc_path, [8,9], 'Согласие на обработку персональных данных.pdf')
		doc_crushing(doc_path, [10,16], 'Договор.pdf')

	if rec != '':
		rec_path = indir + rec

		with pikepdf.open(rec_path) as pdf:
			num_pages = len(pdf.pages)
			if num_pages != 1:
				del_pages(pdf, [1,1], num_pages)

			pdf.save(outdir+'Реквизиты на оплату.pdf')

	if outs:

		for out in outs:

			with pikepdf.open(indir+out) as pdf:

				pdf.save(outdir+out)


if __name__ == '__main__':
	main()