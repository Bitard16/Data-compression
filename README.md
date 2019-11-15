# Data-compression
Data compression +  LZW algorithms

Encoding[edit]
A high level view of the encoding algorithm is shown here:

Initialize the dictionary to contain all strings of length one.
Find the longest string W in the dictionary that matches the current input.
Emit the dictionary index for W to output and remove W from the input.
Add W followed by the next symbol in the input to the dictionary.
Go to Step 2.
A dictionary is initialized to contain the single-character strings corresponding to all the possible input characters (and nothing else except the clear and stop codes if they're being used). The algorithm works by scanning through the input string for successively longer substrings until it finds one that is not in the dictionary. When such a string is found, the index for the string without the last character (i.e., the longest substring that is in the dictionary) is retrieved from the dictionary and sent to output, and the new string (including the last character) is added to the dictionary with the next available code. The last input character is then used as the next starting point to scan for substrings.

In this way, successively longer strings are registered in the dictionary and available for subsequent encoding as single output values. The algorithm works best on data with repeated patterns, so the initial parts of a message see little compression. As the message grows, however, the compression ratio tends asymptotically to the maximum (i.e., the compression factor or ratio improves on an increasing curve, and not linearly, approaching a theoretical maximum inside a limited time period rather than over infinite time).[2]

Decoding[edit]
The decoding algorithm works by reading a value from the encoded input and outputting the corresponding string from the initialized dictionary. To rebuild the dictionary in the same way as it was built during encoding, it also obtains the next value from the input and adds to the dictionary the concatenation of the current string and the first character of the string obtained by decoding the next input value, or the first character of the string just output if the next value can not be decoded (If the next value is unknown to the decoder, then it must be the value added to the dictionary this iteration, and so its first character must be the same as the first character of the current string being sent to decoded output). The decoder then proceeds to the next input value (which was already read in as the "next value" in the previous pass) and repeats the process until there is no more input, at which point the final input value is decoded without any more additions to the dictionary.

In this way, the decoder builds a dictionary that is identical to that used by the encoder, and uses it to decode subsequent input values. Thus, the full dictionary does not need to be sent with the encoded data. Just the initial dictionary that contains the single-character strings is sufficient (and is typically defined beforehand within the encoder and decoder rather than explicitly sent with the encoded data.)


Information from wikipedia
