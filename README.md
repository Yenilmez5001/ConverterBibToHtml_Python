# ConverterBibToHtml_Python
Main task to correctly convert given in.bib file to out.html in a python code

Description:

Convert .bib to .html
Please read important information first.
Description
Your main task is to correctly convert given in.bib file to out.html.
IMPORTANT NOTE: Your code should open the file in.bib and create the file out.html in the same folder. Please make sure your code works only with these filenames.

Input Format
Description of BibTeX entries: https://en.wikipedia.org/wiki/BibTeX
.bib file is composed of items and each item is of the form:
@article{UNIQKEY,
FIELDNAME1 = FIELDCONTENT1,
FIELDNAME2 = FIELDCONTENT2,
….
FIELDNAMEn = FIELDCONTENTn
}
Each item should have a non-empty unique key UNIQKEY which may only contain alphanumeric characters.
Each field should be in a single line.
Empty lines are allowed between items or between fields.
Any line can contain leading or trailing whitespaces.
There may or may not be whitespaces between FIELDNAME, = and FIELDCONTENT
The value FIELDCONTENT should be enclosed either in " " or { }.
FIELDCONTENT should be non-empty.
There will be a comma (,) after each field (except the last field of the item).
Every FIELDNAME should be written in lowercase.
Every item has to contain the fields author, title, journal, year and volume where;
Content of the author field is of the form LASTNAME1, FIRSTNAME1 and LASTNAME2, FIRSTNAME2 and ... and LASTNAMEn, FIRSTNAMEn. The values FIRSTNAME and LASTNAME may only contain alphabetic characters, whitespaces and dots (.).
Content of the title field may only contain alphanumeric characters, whitespaces and the symbols comma (,), dot (.), underscore (_) dash (-), star (*), equals (=), colon (:).
Content of the journal field may only contain alphanumeric characters, whitespaces and the symbols comma (,), dot (.), underscore (_).
Content of the year field should be a 4 digit positive number where it is a valid year (starts with either 1 or 2).
Content of the volume field should be a positive number.
Additionally, every item may or may not contain the fields number, pages and doi where;
Content of the number field should be a positive number.
Content of the pages should have the following form START--END. Values START and END are positive numbers separated by a double dash (--).
Content of the doi field should have the following form PREFIX/SUFFIX. Values PREFIX and SUFFIX are separated by a forward slash (/) and may only contain alphanumeric characters and dot (.).
Fields can be given in any order.
Output Format
If the given input file in.bib do not follow the format described above, output file should only contain the text Input file in.bib is not a valid .bib file!.
General form (with optional fields) of an item in a .bib file:
@article{UNIQKEY,
author= "AUTHOR",
title={TITLE},
  journal = "JOURNAL",   


year = {YEAR},     
volume=   {VOLUME},
number = "NUMBER",
pages = {PAGES},
doi = {DOI}
}
or
@article{UNIQKEY,
author = {AUTHOR},
title = "TITLE",
journal =     "JOURNAL",


year ="YEAR",
volume = {VOLUME},
number = {NUMBER},
  pages={PAGES},

  doi   =   "DOI"  
}
The corresponding .html file should list the items in descending year order. For the items that have the same year, sort them with respect to their title strings in ascending order (ascii sorting).
A general form of the output is as follows:
<html>
<br> <center> <b> YEAR </b> </center>
<br>
[J1] FIRSTNAME1 LASTNAME1, FIRSTNAME2 LASTNAME2, FIRSTNAME3 LASTNAME3... and FIRSTNAMEn LASTNAMEn, <b>TITLE</b>, <i>JOURNAL</i>, VOLUME[:NUMBER][, pp. PAGES], <YEAR>. [<a href="https://doi.org/DOI">link</a>] <br>
….
</html>
Each item in the output starts with the prefix [Ji] where i is the order in which the item appears in the output file (bottommost item is [J1]).
We have provided you with three example input (ex_in1.bib, ex_in2.bib, ex_in3.bib and ex_in4.bib) and output (ex_out1.html, ex_out2.html, ex_out3.html and ex_out4.html) files. Check the examples for further clarification.
Please note that given examples do not cover all of the possible cases. Your code should be able to handle other cases as well.
