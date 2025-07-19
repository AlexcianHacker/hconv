rom typing import TextIO, Any; from ctypes import c_void_p; import sys;  
def converter(file) -> int: 
    if file.__class__ == str: 
        dent: str = file; 
        del file; 
    else: 
        dent: list[str] = file.readlines(); 
        del file; 
    res: str = ""; 
    for line in dent: 
        pres: str = "" 
        for x in line: pres += str(ord(x))  
        res += str(hex(int(pres))) 
    try: print(res); del res; 
    except: return 1; 
    return 0; 

if __name__=="__main__": 
    num: int = 0; 
    if sys.argv[0] == sys.argv[-1]:  
        fn: str = str(input("Enter File Name For Hex Conversion: ")); fle = open(fn, "r"); 
        while converter(fle) != 0 and num < 5: num+=1; 
        fle.close() 
        if num != 0: print("There May Have Been An Issue During The Hex Conversion."); 
    else: ## 2nd Option To Receive Str Instead Of File 
        rec: str = input("Enter String To Convert To Hex: "); 
        while converter(rec) != 0 and num < 5: num+=1; 
        if num != 0: print("There May Have Been An Issue During The Hex Conversion."); 
