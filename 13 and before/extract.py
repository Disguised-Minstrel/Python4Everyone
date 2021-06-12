string = 'X-DSPAM-Confidence: 0.8475 '

sub = string[string.find(':')+1:]
sub = float(sub.strip())
print(sub, type(sub))
