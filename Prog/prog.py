def has_two_recurring_chars(string):
    chars = set(string)
    return len(chars) < len(string)

i = 0
o = 0
line = "nfddjzjjjmrjjfttzctzzhqzqbbvhhcfcpcqpcqpccsmsvsswbwzwfffnvfvpfvffhnnrgngzgrrhvhfhvvmjvjcccvppqdppbnbjjzlzflfccjjtctqccrhrnhnqhqwwjssjjhpjjcqqdgghddhfdfbffdpfdfzdddthhrcrbrqrbqqbcbnnwbbzcbzccmqqwllrljjjpqpdpsddmbmccwwgngmmzzzpbpspnprnppprmmwfwffrrpsrrchrrrrdqdfddnvnjnppqmqhhpshhjmhjhzjhhhzllbpbnnngdgzgmmjvvprrhqrhqhpqhqqrnqnddvjvvftfggfcgfffgrghhbmbzzjczzcscrccgbbjbqjbjsbsqbqttbqbfqqqrzrmzrmmcwcmwmrwmwnmnfnjjbdjbbslltjjmgmrmllhbhsbsmsqmqllvjjrvjrjcrrtztjzjbjsbbrjjvbjjgqjjpjsszpszsnznllvmlmfmppbvbzvvddtbtrbttchthjthjhnjnqnqrrllnflnnljnnzjjswjwllpmmpnnqnrrndnnbwwmcmcmbbhjjbbfpfvpvttcvvhshqqznzqqdndldmllpgptgptpbblzlddgqqdmmvpvvrccfvvjrvjjgpggqcggjbgbqqcgqccgppffjppzczmzdmmqppwcwlcwwhccfpcphcctvtzthtzhhnmnvmnnvqnqnpnqqwqsqdsszwzbwwgcwcrrtprrfhhcmcqcdcvdcccnpptgpgwpprsprsrdrtdrtrntrtprtppstsccbwwvnvpnvpnptpqttzbzcznzhzhddfbflfcchvchhplhlwhhlhglhhwqqzlqzlzvlvtlvtvrttglttslslclslqssslclbbrjrpjjcscfsfppjlplhplptlltlflglffdttmffrggfjjmllbnlnbnznqnfffmhhnmmsgmsmfsszggpnnhmhnnpwnndqqlmqmnmtnmtnttvtztlzlnzzsdsnssvhsszcscffcpczpcpffpwfwnwhnntnssptthccbnndppgjgpjpssbnnpgnpppjtjqqzfqqrrbmmbdddzjzvzwzssnpsnspnpvnpppjppvsvffmpffbcffslfsfmsmmqzzmttnsnqsqcsqsbqbcclqqphpttvrtrlrhrthhlppscsrsjjvljlmlwlslblqqqgdsbrzwzjzwcjrwbpfmjtmdgjvbcfvtvmsfjtjcmtlzmsjlnmhcswcmjndggdsmqfmmdngjpvrsbhrchldnhdhfdlwccnfmgbwfzppgzzcvblvsmqbfghrgdwlzdcvpqthgbdlwbrfpsvlgpdqznftswgwvchjfrblbdsqjmzchfhlrjhpbrdgvgrrmhrnrdbrdsfsgzvqfdtnvddbtcjwphrhgpqlzjssrgzjcncjnbrzvhgbwpgtfnqhpspmgptzcgvjqgzpmwtjtzldqnclmplwdpzcppgcbrsnlzfgmlnljjhfzrftnhdfnqchgdqrfcjszvbmdrghwzmjnwgnrlptljzqrwsmcfwvbcjgsfdjhnqgzzztmcgmndbtdwvqmzlfcmhfgpqztwgjdccncdccpgbcvhfzbhhbjhgjpdzcmrwgtvrmzdwjtmlzllmgplpqjwwwvbrzgmvpcvwchcwfgbjtzrfctgvfrpphbnsbjlswrztqmchtzfstzdgdwwvhpdhztbmsrbqmndpgvnwwdtgzcddvmvbjstqmjvtzlzgrhzhvplwnpphctvtlvnpmwfzmqcvrnfmmgtsgbcjpffrvbpqpszfpjsjtzqmcnzhnjnpwtvgfqntnhhjhmbvmlvmqgggrnfmmmsvfsqffbvwtzlfhlbjqhrltzwfstvjqhbbblqdbcmgtjgmzdtpslbzsgnmpzsswjlwdpzpmmvmpntbhnqlwrcrfbghzhwlhhpjqztjjrrfscrtwtnlqlqmdbmbfnvngvvthhghgsvqlqvgvmtjmjtwpcznzqhhfpqqfphcdrtzjjhsffslthzwpmsnltnjmfgpsjgqzdwrtgnhflhrnjwqftpnqgptgvgjptzhhtqhtddsfhppmmqcrsnlnrswpjhqgzbpwzfzptzqzzwltlrmjwjrwdgvvzhshqqrhtzmvqpfljlvpmrzbqpscpvsfdbdbcbdwwhpmldlrgpwslzhtbpgtzscfhjlgwcgbhcbftpftvpggvcdvndqnfvfqbwrjtdcbwpsbqpzmwdhjpmjhjmlcdphrjbgsnmcmvfnrggfvttclmbvsfjpnbndbblnbdfqzmsldlswdrtzqsqppjshtlrtccthmmpjgddbbgfgthnzdffbtrpchzgbvqvjcsnpgbrzrczzmzrmhjrlvvgmsqddjsqmcqfmwnhznbczzjlpmhnfwjtrfgffsjdlwgdwwlvdpdlvszphntrvttczgnwffsdsvjmqbthgcgfjgznrfnbplbvgsjbsglhnrjpbldhmznqgqpvldvhcpmmwzfjdjdbnprtrrnwsszjhmngvmtsrqdqdsprwhjpsqwqbsdtpptwlbfbsvdgrplrvpnfbzwrdsdbvhpgwcnqvwdcswdmdltchnngpmlqvchbnrpzcnfhvlzbwbnmssbhpvvmpcwvrwzpfpssndwwfnrslpjwhwrfsswmgtszrhczcrclpldpwpghgptmzzjjjtvjcnncjpfbcvldbnlnqtsqdswcsrqcfgvwbwdvbdwwzndfvcstjbfngtqqwsbpdjdgqdlsnwgcvmmhrqcqvdbqdqczzwzlfgffbwzbfdnpvprzmqclllsdvctwjfgqbchhmsntlvnlspwtnhgshwrvzccfmfrscqwrvdccwqnrccctjrvvnqbrphrfvfrfldbbthhrdzvdmfbctsmvgwmvpdslgbcpqqdvpsjcdvmctwghdsjtmhhvdswbcvtmsnsztfghnnfhflmmnmdqpvpdplllzgqgnsjwsrgzfwhrwhcscvrgcrgjdghqjfbswtgjsvnpqznrvbdbrplwdmbqhtbcfccnpwqlsdstnpcfpbfgqrzmcqhflmcfvbbnwrrblnfslsrwpwlbvqfhgpdwzmgvftssrvdmhnmwdfqmsvqbltlmmwmjrrhgpgznqbwhcqgphvzqmntbbdhhpnlbbffjgmcdntgwmtblwlzrcdcdbtrllrdnznrrsglnwhtwbrfdrpvgqwsgzwghbtsfwqlchgsnvfmvnzntlsnlwrnjjltrpmhwnzmhrqdlvvzbfgwlwgdsgcjcjfvhbcjgzlqtsljvzcvlppqdszvdbsmgddrtmvbcpbpppcpvhzfsjrmtcpzljbhpnjjmcdwslrhslccpljrtvcscbcltpshpnrqvtdfzbbfqtpbvznvrbflwvbvrhqpzltsdrnqccsfgzzftvjfqslcnmfvwtpdbjhtzwrgvntgnfvqtdrjdgglvrnqfzsbhnvhcdbctthdrjnvwlcsjtmphpvlqjngwjnngmqqnslrrsdfpfbvsvcwjtfmwtbpnnghtvvwlphbnsgflvsfdcqrctvjfjrwqjdmbbcclwvlstbgbfqjgbpbqfwdbpmnvqnfpbhrfhwltmcszpwnvtvhrvpcqhzdppjwttlhgsnvmsrwrnwvgzpbwljjjsjzctftzftvmsstpjnzvmmrgbbpmfmfrszwjdgzfhpvsfdqbbhgvfvqrrtqwlwzwwsnnmmvmlwjzvgrwhmffzwrqwbcdtbtzpspbnqgprdqtzrpmgvnmbsnjnvtzgmhqqtrvltbsrwjlssncdppgpmzqzbzvbpjpfwmvgsbhffzpbctmqvfwhsgdjtwqhrhmgnqpvmpjzhppvcbrpwmdshzcrwzdzcjmhfvjgtbznsmdjphlssmlmbhtmnsqnjfsjwhjvgztnwhmnztqppchngdnhzwpsvqqpzdwgbhcbzvmbnqmghbhgvrqhtfzhgvqdbpvdrjsqrdnhqhrwdlczvtnzwfrqhnffwdvtrnqsmmcjtrhmgbwcmnzbbvdsrlbbtwslhghwprpglpq"
while o!=1:
    first = line[i:i+14]
    if has_two_recurring_chars(first):
        i+=1
    else:
        o+=1
print(i)

