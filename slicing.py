text = "X-DSPAM-Confidence:    0.8475"
num = text[text.find("0.8475"):text.find("0.8475") + 6]
data = float(num)
print data, type(data)