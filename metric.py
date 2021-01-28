# Things to be able to handle: mass or units/volume (check), different denominators in mass or units/volume (check), molarity(check), conversion from mass/volume to molarity and vise versa (check), mass percentage (check), parts per thousand (check), parts per million (check), and parts per billion (check).
#preamble
def iup() :
    global inp
    inp = inp/1000
def iup10() :
    global inp
    inp = inp/10
def idown() :
    global inp
    inp = inp*1000
def idown10() :
    global inp
    inp = inp*10
def oup() :
    global out
    out = out/1000
def oup10() :
    global out
    out = out/10
def odown() :
    global out
    out = out*1000
def odown10() :
    global out
    out = out*10
def inconc() :
    global sconc
    global unit
    conc = sconc
    while conc != unit :
        if conc[0] == 'm' :
            iup()
            conc = unit
        elif conc[0] == 'k':
            idown()
            conc = unit
        elif conc[0] == 'd' :
            if conc[0:2] == 'da' :
                idown10()
                conc = unit
            else :
                iup10()
                conc = unit
        elif conc[0] == 'h' :
            iup10()
            conc = 'k' + unit
        elif conc[0] == 'c' :
            idown10()
            conc = 'm' + unit
        elif conc[0] == 'µ' :
            iup()
            conc = 'm'+ unit
        elif conc[0] == 'u' :
            iup()
            conc = 'm'+ unit
        elif conc[0] == 'n' :
            iup()
            conc = 'u'+ unit
        elif conc[0] == 'p' :
            if conc[0:2] == 'pp':
                conc = unit
                break
            iup()
            conc = 'n'+ unit
        elif conc[0] == 'f' :
            iup()
            conc = 'p'+ unit
        elif conc[0] == 'a' :
            iup()
            conc = 'f'+ unit
        elif conc[0] == 'M' :
            idown()
            conc = 'k'+ unit
        elif conc[0] == 'G' :
            idown()
            conc = 'M'+ unit
        elif conc[0] == 'T' :
            idown()
            conc = 'G'+ unit
        elif conc[0] == 'P' :
            idown()
            conc = 'T'+ unit
        elif conc[0] == 'E' :
            idown()
            conc = 'P'+ unit
        else :
            print ('Starting concentration prefix not accepted, please try again.')
            metric_conversion()
            break
def outconc() :
    global econc
    global endunit
    conc = econc
    while conc != endunit :
        if conc[0] == 'm' :
            oup()
            conc = endunit
        elif conc[0] == 'k':
            odown()
            conc = endunit
        elif conc[0] == 'd' :
            if conc[0:2] == 'da' :
                odown10()
                conc = endunit
            else :
                oup10()
                conc = endunit
        elif conc[0] == 'h' :
            oup10()
            conc = 'k' + unit
        elif conc[0] == 'c' :
            odown10()
            conc = 'm' + unit
        elif conc[0] == 'µ' :
            oup()
            conc = 'm'+ unit
        elif conc[0] == 'u' :
            oup()
            conc = 'm'+ unit
        elif conc[0] == 'n' :
            oup()
            conc = 'u'+ unit
        elif conc[0] == 'p' :
            oup()
            conc = 'n'+ unit
        elif conc[0] == 'f' :
            oup()
            conc = 'p'+ unit
        elif conc[0] == 'a' :
            oup()
            conc = 'f'+ unit
        elif conc[0] == 'n' :
            oup()
            conc = 'u'+ unit
        elif conc[0] == 'M' :
            odown()
            conc = 'k'+ unit
        elif conc[0] == 'G' :
            odown()
            conc = 'M'+ unit
        elif conc[0] == 'T' :
            odown()
            conc = 'G'+ unit
        elif conc[0] == 'P' :
            odown()
            conc = 'T'+ unit
        elif conc[0] == 'E' :
            odown()
            conc = 'P'+ unit
        else :
            print ('Ending concentration prefix not accepted, please try again.')
            metric_conversion()
            break
def common_denominator() :
    global indenominator
    global innumerator
    global outdenominator
    global outnumerator
    global sconc
    while indenominator != outdenominator :
        if indenominator[0] == 'm' :
            if outdenominator[0] == 'u' :
                iup()
                indenominator = 'u'+outdenominator[1:10]
            elif outdenominator[0] == 'n' :
                iup()
                iup()
                indenominator = 'n'+outdenominator[1:10]
            elif outdenominator == 'l' :
                idown()
                indenominator = 'l'
            else :
                print ('Starting concentration denominator and ending concentration denominator are outside of set conversion range (L-nL). Please try again.')
                metric_conversion()
                break
        elif indenominator[0] == 'u' :
            if outdenominator[0] == 'n' :
                iup()
                indenominator = 'n'+outdenominator[1:10]
            elif outdenominator[0] == 'm' :
                idown()
                indenominator = 'm'+outdenominator[1:10]
            elif outdenominator == 'l' :
                idown()
                idown()
                indenominator = 'l'
            else :
                print ('Starting concentration denominator and ending concentration denominator are outside of set conversion range (L-nL). Please try again.')
                metric_conversion()
                break
        elif indenominator[0] == 'µ' :
            if outdenominator[0] == 'n' :
                iup()
                indenominator = 'n'+outdenominator[1:10]
            elif outdenominator[0] == 'm' :
                idown()
                indenominator = 'm'+outdenominator[1:10]
            elif outdenominator == 'l' :
                idown()
                idown()
                indenominator = 'l'
            else :
                print ('Starting concentration denominator and ending concentration denominator are outside of set conversion range (L-nL). Please try again.')
                metric_conversion()
                break
        elif indenominator[0] == 'n' :
            if outdenominator[0] == 'u' :
                idown()
                indenominator = 'u'+outdenominator[1:10]
            elif outdenominator[0] == 'm' :
                idown()
                idown()
                indenominator = 'm'+outdenominator[1:10]
            elif outdenominator == 'l' :
                idown()
                idown()
                idown()
                indenominator = 'l'
            else :
                print ('Starting concentration denominator and ending concentration denominator are outside of set conversion range (L-nL). Please try again.')
                metric_conversion()
                break
        elif indenominator == 'l' :
            if outdenominator[0] == 'u' :
                iup()
                iup()
                indenominator = 'u'+outdenominator[1:10]
            elif outdenominator[0] == 'm' :
                iup()
                indenominator = 'm'+outdenominator[1:10]
            elif outdenominator[0] == 'n' :
                iup()
                iup()
                iup()
                indenominator = 'n'+outdenominator[1:10]
            else :
                print ('Starting concentration denominator and ending concentration denominator are outside of set conversion range (L-nL). Please try again.')
                metric_conversion()
                break
    sconc = innumerator + '/' + indenominator
def mnv_to_molar() :
    global molweight
    global indenominator
    global inp
    global unit
    global sconc
    units = ['%', 'M', 'g/L', 'g/mL', 'g/uL', 'g/µL', 'g/nL', 'ppb', 'ppm', 'ppt', 'g/l', 'g/ml', 'g/ul', 'g/µl', 'g/nl', 'U/ml', 'U/l', 'U/ul', 'U/µl', 'U/nl', 'U/L', 'U/mL', 'U/uL', 'U/µL', 'U/nL']
    if indenominator[0] == 'm' :
        idown()
        indenominator = 'l'
    elif indenominator[0] == 'u' :
        idown()
        idown()
        indenominator = 'l'
    elif indenominator[0] == 'µ' :
        idown()
        idown()
        indenominator = 'l'
    elif indenominator[0] == 'n' :
        idown()
        idown()
        idown()
        indenominator = 'l'
    else :
        print ('Starting concentration denominator not accepted. (accepted: nL-L) Try again.')
        metric_conversion()
    inp = inp/molweight
    unit = 'M'
    if sconc[0:2] == 'da' :
        sconc = sconc[0:2]+unit
    elif sconc in units :
        sconc = unit
    else :
        sconc = sconc[0]+unit
def molar_to_mnv() :
    global molweight
    global outdenominator
    global out
    global endunit
    if outdenominator[0] == 'm' :
        odown()
        outdenominator = 'l'
    elif outdenominator[0] == 'u' :
        odown()
        odown()
        outdenominator = 'l'
    elif outdenominator[0] == 'µ' :
        odown()
        odown()
        outdenominator = 'l'
    elif outdenominator[0] == 'n' :
        odown()
        odown()
        odown()
        outdenominator = 'l'
    else :
        print ('Ending concentration denominator not accepted. (accepted: nL-L) Try again.')
        metric_conversion()
    out = out/molweight
    endunit = 'M'
def parts() :
    #convert 'parts per ___' among each other
    global unit
    global endunit
    if unit != endunit :
        if unit[-1] == 'b' :
            if endunit[-1] == 'm' :
                iup()
                unit = 'ppm'
            if endunit[-1] == 't' :
                iup()
                iup()
                unit = 'ppt'
        elif unit[-1] == 'm' :
            if endunit[-1] == 'b' :
                idown()
                unit = 'ppb'
            if endunit[-1] == 't' :
                iup()
                unit = 'ppt'
        elif unit[-1] == 't' :
            if endunit[-1] == 'm' :
                idown()
                unit = 'ppm'
            if endunit[-1] == 'b' :
                idown()
                idown()
                unit = 'ppb'
def metric_conversion() :
    global indenominator
    global innumerator
    global outnumerator
    global outdenominator
    global D
    global sconc
    global inp
    global econc
    global out
    global unit
    global endunit
    global molweight
    units = ['%', 'M', 'g/L', 'g/mL', 'g/uL', 'g/µL', 'g/nL', 'ppb', 'ppm', 'ppt', 'g/l', 'g/ml', 'g/ul', 'g/µl', 'g/nl', 'U/ml', 'U/l', 'U/ul', 'U/µl', 'U/nl', 'U/L', 'U/mL', 'U/uL', 'U/µL', 'U/nL']
    mnv = ['g/L', 'g/mL', 'g/uL', 'g/µL', 'g/nL', 'g/l', 'g/ml', 'g/ul', 'g/µl', 'g/nl']
    #receive starting and ending concentration; receive unit
    inp, sconc = input ('What is your starting concentration? (## units): ').split()
    inp = D (inp)
    #separate fractional units
    if '/' in sconc :
        innumerator, indenominator = sconc.split('/')
    #account for deka, the only two letter metric prefix
    if sconc[0:2] == 'da' :
        unit = sconc[2:5]
    #account for prefix-less units
    elif sconc in units :
        unit = sconc
    else:
        unit = sconc[1:5]
    out, econc = input ('What is your desired concentration? (## units): ').split()
    out = D (out)
    #separate fractional units
    if '/' in econc :
        outnumerator, outdenominator = econc.split('/')
    #account for deka, the only two letter metric prefix
    if econc[0:2] == 'da' :
        endunit = econc[2:5]
    #account for prefix-less units
    elif econc in units :
        endunit = econc
    else:
        endunit = econc[1:5]
    #account for 'parts per ____' discrepancies
    if unit[0:2] == 'pp' :
        parts()
    if '/' in sconc :
        #account for fractional units with different denominators
        try:
            if indenominator != outdenominator :
                common_denominator()
                if sconc in units :
                    unit = sconc
        #account for conversion from mass/volume to molarity
        except:
            if endunit == 'M' :
                molweight = input('What is the molecular weight of the substance in solution? ')
                molweight = D (molweight)
                mnv_to_molar()
    #account for conversion from molarity to mass/volume
    if '/' in econc :
        if unit == 'M' :
            molweight = input('What is the molecular weight of the substance in solution? ')
            molweight = D (molweight)
            molar_to_mnv()
    #handle discression in starting and ending units which are unaccounted for.
    if unit != endunit :
        print ('Incompatable inputs for starting and ending concentrations. Please try again.')
        metric_conversion()
    else:
        #Convert start and end concentrations to base unit
        inconc()
        outconc()
        #Identify relationship between in and out values
        inp = D (inp)
        out = D (out)
        dil = inp/out
        #Deal with end concentrations which are higher than start concentrations
        if dil < 1 :
            print ('Cannot concentrate solution. Starting concentration must be greater than desired concentration.')
            metric_conversion()
        #Indicate best dilution practice
        else :
            print ('\nStart:', inp, unit)
            count = 0
            while dil >= 100 :
                count = count + 1
                dil = dil/100
            if dil < 10 :
                if count != 0 :
                    count = count - 1
                    dil = D (dil)
                    dil = dil*10
                    print ('1:10')
            if count > 0 :
                count = str(count)
                print ('1:100 x' + count)
            dil = str(dil)
            if 'E+2' in dil :
                dil = int(dil[0])*100
                dil = str(dil)
            if 'E+1' in dil :
                dil = int(dil[0])*10
                dil = str(dil)
            if dil == '0' :
                print ('End:', out, endunit)
                print ('Thanks!\n')
            if dil == '1' :
                print ('End:', out, endunit)
                print ('Thanks!\n')
            else :
                print ('1:'+dil)
                print ('End:', out, endunit)
                print ('Thanks!\n')
            #Do you want to keep checking conversions?
            end = input ('Go again?(y/n) ')
            if end == 'y' :
                metric_conversion()
            elif end == 'yes' :
                metric_conversion()
            elif end == 'no' :
                print ('All done!\n')
            elif end == 'n' :
                print ('All done!\n')
#fix python's weird float decimals
import decimal
D = decimal.Decimal
#core program
metric_conversion()
#test text
