def bill_total(lst):
    total_amount = 0
    for items in lst:
        if items<100:
            total_amount += items

        elif(items>=100 and items<500):
            total_amount += (items-(items*0.05))

        elif(items>=500 and items<1000):
            total_amount+=(items-(items*0.10))
        
        elif(items>=1000 and items <1500):
            total_amount+=(items-(items*0.15))
        
        else:
            total_amount+=(items-(items*0.20))
        
    return round(total_amount)


def amount_to_words(total_amount):
    ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
            "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

    tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

    if total_amount == 0:
        return "Zero"
    
    elif total_amount <20:
        return ones[total_amount]
    
    elif total_amount<100:
        return tens[total_amount//10] + " " + ones[total_amount%10]
    
    elif total_amount<1000:
        return ones[total_amount//100] + " Hundred " + amount_to_words(total_amount%100)

    elif total_amount<10000:
        return ones[total_amount//1000] + " Thousand " + amount_to_words(total_amount%1000)
    
    else:
        return "Invalid Input"


lst = list(map(int,input("enter the items price here : ").split()))

result = bill_total(lst)
print("Total amount :",result)
print("Amount in words :",amount_to_words(result))

#input : 120 80 450 600 1500
#output : Total amount : 2565
#         Amount in words : Two Thousand Five Hundred Sixty Five