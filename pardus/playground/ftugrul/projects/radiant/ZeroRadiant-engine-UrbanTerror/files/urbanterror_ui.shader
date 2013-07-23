//  MAIN LINES		 //



ui_lines1
{	
	nopicmip
	nomipmaps
	{
		map ui/assets/ui_lines1.tga
		blendfunc add
		rgbgen identity
		tcmod scroll .02 0
	}
}

ui_lines2
{	
	nopicmip
	nomipmaps
	{
		map ui/assets/ui_lines2.tga
		blendfunc add
		rgbgen identity
		tcmod scroll -.02 0
	}
}

//  MAIN CIRCLE		 //

models/misc/circle_1
{
	{
		map models/misc/circle_1.tga
		blendFunc add
//		blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
		rgbGen identity
	}
}
