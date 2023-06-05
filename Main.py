

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

f_handle = open('in.bib', 'r')
content = f_handle.read().strip()
article_dict = {}
bib = True
u_key_list = []
while content != '':
    content = content.strip()
    if content.startswith('@article{'):
        content = content[9:]
        unique_key = content[:content.index(',')]
        u_key_list.append(unique_key)
        if not unique_key.isalnum():
            bib = False
            break
        content = content[content.index(',') + 2:]
        inside_info = content[:content.index('\n}') + 2]
        content = content[content.index('\n}') + 2:].strip()

        inside_dict = {}
        while inside_info != '':
            inside_info = inside_info.strip()

            if inside_info.lower().startswith("author"):
                for i in inside_info[:6]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                author_line = inside_info[6:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not author_line.startswith('='):
                    bib = False
                    break

                if not author_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        author_line = author_line[1:].strip()

                if author_line.endswith(','):
                    author_line = author_line[1:-1].strip()

                if author_line.startswith('"') and author_line.endswith('"'):
                    authors = author_line.strip('"').strip()
                elif author_line.startswith('{') and author_line.endswith('}'):
                    authors = author_line.strip('{}').strip()
                else:
                    bib = False
                    break

                for i in authors:
                    if not (i in '""{}., ' or i.isalpha()):
                        bib = False
                        break
                inside_dict['author'] = authors

            inside_info = inside_info.strip()
            if inside_info.lower().startswith('volume'):
                for i in inside_info[:6]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                volume_line = inside_info[6:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not volume_line.startswith('='):
                    bib = False
                    break

                if not volume_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        volume_line = volume_line[1:].strip()

                if volume_line.endswith(','):
                    volume_line = volume_line[1:-1].strip()
                if volume_line.startswith('"') and volume_line.endswith('"'):
                    volume = volume_line.strip('"').strip()
                elif volume_line.startswith('{') and volume_line.endswith('}'):
                    volume = volume_line.strip('{}').strip()
                else:
                    bib = False
                    break
                try:
                    volume = int(volume)
                    if not volume > 0:
                        bib = False
                        break
                except ValueError:
                    bib = False
                    break
                inside_dict['volume'] = str(volume)

            inside_info = inside_info.strip()
            if inside_info.lower().startswith("title"):
                for i in inside_info[:5]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                title_line = inside_info[5:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not title_line.startswith('='):
                    bib = False
                    break

                if not title_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        title_line = title_line[1:].strip()
                if title_line.endswith(','):
                    title_line = title_line[1:-1].strip()

                if title_line.startswith('"') and title_line.endswith('"'):
                    title = title_line.strip('"').strip()
                elif title_line.startswith('{') and title_line.endswith('}'):
                    title = title_line.strip('{}').strip()
                else:
                    bib = False
                    break
                for i in title:
                    if not (i.isalnum() or i in ' ,._-*=:'):
                        bib = False
                        break
                inside_dict['title'] = title

            inside_info = inside_info.strip()
            if inside_info.lower().startswith('year'):
                for i in inside_info[:4]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                year_line = inside_info[4:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not year_line.startswith('='):
                    bib = False
                    break

                if not year_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        year_line = year_line[1:].strip()

                if year_line.endswith(','):
                    year_line = year_line[1:-1].strip()
                if year_line.startswith('"') and year_line.endswith('"'):
                    year = year_line.strip('"').strip()
                elif year_line.startswith('{') and year_line.endswith('}'):
                    year = year_line.strip('{}').strip()
                else:
                    bib = False
                    break
                try:
                    year = int(year)
                    if not year > 0:
                        bib = False
                        break
                except ValueError:
                    bib = False
                    break

                if len(str(year)) == 4:
                    if str(year)[0] == '1' or str(year)[0] == '2':
                        inside_dict['year'] = str(year)
                    else:
                        bib = False
                        break
                else:
                    break

            inside_info = inside_info.strip()
            if inside_info.lower().startswith('number'):
                for i in inside_info[:6]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                number_line = inside_info[6:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not number_line.startswith('='):
                    bib = False
                    break

                if not number_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        number_line = number_line[1:].strip()

                if number_line.endswith(','):
                    number_line = number_line[1:-1].strip()
                if number_line.startswith('"') and number_line.endswith('"'):
                    number = number_line.strip('"').strip()
                elif number_line.startswith('{') and number_line.endswith('}'):
                    number = number_line.strip('{}').strip()

                else:
                    bib = False
                    break
                try:
                    number = int(number)
                    if not number > 0:
                        bib = False
                        break
                except ValueError:
                    bib = False
                    break
                inside_dict['number'] = str(number)

            inside_info = inside_info.strip()
            if inside_info.lower().startswith('doi'):
                for i in inside_info[:3]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                doi_line = inside_info[3:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not doi_line.startswith('='):
                    bib = False
                    break

                if not doi_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        doi_line = doi_line[1:].strip()

                if doi_line.endswith(','):
                    doi_line = doi_line[1:-1].strip()
                if doi_line.startswith('"') and doi_line.endswith('"'):
                    doi = doi_line.strip('"').strip()
                elif doi_line.startswith('{') and doi_line.endswith('}'):
                    doi = doi_line.strip('{}').strip()

                else:
                    bib = False
                    break

                if doi.count('/') == 1:

                    if doi[-1] != '/' or doi[0] != '/':
                        prefix = doi.split('/')[0]
                        suffix = doi.split('/')[-1]
                        for i in prefix + suffix:
                            if not (i.isalnum() or i == '.'):
                                bib = False
                                break
                        else:
                            inside_dict['doi'] = doi
                    else:
                        bib = False
                        break
                else:
                    bib = False
                    break
                if not bib:
                    break

            inside_info = inside_info.strip()
            if inside_info.lower().startswith("journal"):
                for i in inside_info[:7]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                journal_line = inside_info[7:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not journal_line.startswith('='):
                    bib = False
                    break

                if not journal_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        journal_line = journal_line[1:].strip()
                if journal_line.endswith(','):
                    journal_line = journal_line[1:-1].strip()

                if journal_line.startswith('"') and journal_line.endswith('"'):
                    journal = journal_line.strip('"').strip()
                elif journal_line.startswith('{') and journal_line.endswith('}'):
                    journal = journal_line.strip('{}').strip()
                else:
                    bib = False
                    break
                for i in journal:
                    if not (i.isalnum() or i in ' ,._'):
                        bib = False
                        break
                inside_dict['journal'] = journal

            inside_info = inside_info.strip()
            if inside_info.lower().startswith('pages'):
                for i in inside_info[:5]:
                    if i == i.upper():
                        bib = False
                        break
                if not bib:
                    break

                pages_line = inside_info[5:inside_info.index('\n')].strip()
                inside_info = inside_info[inside_info.index('\n'):]
                if not pages_line.startswith('='):
                    bib = False
                    break

                if not pages_line.endswith(','):
                    if not inside_info[inside_info.index('\n') + 1] == '}':
                        bib = False
                        break
                    else:
                        inside_info = ''
                        pages_line = pages_line[1:].strip()

                if pages_line.endswith(','):
                    pages_line = pages_line[1:-1].strip()
                if pages_line.startswith('"') and pages_line.endswith('"'):
                    pages = pages_line.strip('"').strip()
                elif pages_line.startswith('{') and pages_line.endswith('}'):
                    pages = pages_line.strip('{}').strip()

                else:
                    bib = False
                    break

                if pages.count('--') == 1:

                    if pages[-1] != '--' or pages[0] != '--':
                        start_page = pages.split('--')[0]
                        end_page = pages.split('--')[-1]

                        for i in start_page + end_page:
                            if not i.isnumeric():
                                bib = False
                                break
                        else:
                            if start_page == '0' or end_page == '0':
                                bib = False
                                break
                            inside_dict['page'] = pages
                    else:
                        bib = False
                        break
                else:
                    bib = False
                    break
                if not bib:
                    break

        article_dict[unique_key] = inside_dict
    else:
        bib = False
        break
for item in article_dict.values():
    if not ('author' in item and 'journal' in item and 'title' in item and 'volume' in item and 'year' in item):
        bib = False
        break

for u_key in u_key_list:
    if u_key_list.count(u_key) != 1:
        bib = False
        break

if not bib:
    writing_error_handle = open('out.html', 'w')
    writing_error_handle.write('Input file in.bib is not a valid .bib file!')
    writing_error_handle.flush()
    writing_error_handle.close()

else:
    def comp(unique_key_):
        return -int(article_dict[unique_key_]['year']), article_dict[unique_key_]['title']

    unique_key_list = list(article_dict.keys())
    unique_key_list.sort(key=comp)

    big_name_list = []
    for sorted__key in unique_key_list:
        author_names = article_dict[sorted__key]['author'].split(' and ')
        big_name_list.append(author_names)

    big_sorted_name_list = []
    for liste in big_name_list:
        names_in_article = []
        for surname_name in liste:
            name = surname_name.split(', ')[-1]
            surname = surname_name.split(', ')[0]
            names_in_article.append(' ' + name + ' ' + surname + ',')
        big_sorted_name_list.append(names_in_article)

    for name_surname_list in big_sorted_name_list:
        if len(name_surname_list) > 1:
            name_surname_list[-2] = name_surname_list[-2][:-1] + ' and'

    names_for_write = []
    for i in big_sorted_name_list:
        s = ''
        for j in i:
            s += j
        names_for_write.append(s)

    html_starting_tag = '<html>\n'
    html_ending_tag = '</html>'
    year_s_tag = '<br> <center> <b> '
    year_end_tag = ' </b> </center>\n'
    content_to_be_written = html_starting_tag
    a = ''
    my_index = 0
    for sorted_key in unique_key_list:
        if a != article_dict[sorted_key]['year']:
            content_to_be_written += year_s_tag + article_dict[sorted_key]['year'] + year_end_tag
            content_to_be_written += '<br>\n' + '[J' + str(len(article_dict)-my_index) + ']' + names_for_write[my_index] + ' <b>' + article_dict[sorted_key]['title'] + '</b>,'
            content_to_be_written += ' <i>' + article_dict[sorted_key]['journal'] + '</i>, ' + article_dict[sorted_key]['volume']
            if 'number' in article_dict[sorted_key]:
                content_to_be_written += ':' + article_dict[sorted_key]['number']
            if 'page' in article_dict[sorted_key]:
                content_to_be_written += ', pp. ' + article_dict[sorted_key]['page'].replace('--', '-')
            content_to_be_written += ', ' + article_dict[sorted_key]['year'] + '. '
            if 'doi' in article_dict[sorted_key]:
                content_to_be_written += f"<a href=\"https://doi.org/{article_dict[sorted_key]['doi']}\">link</a> "
            content_to_be_written += '<br>\n'

        else:
            content_to_be_written += '<br>\n' + '[J' + str(len(article_dict)-my_index) + ']' + names_for_write[my_index] + ' <b>' + article_dict[sorted_key]['title'] + '</b>,'
            content_to_be_written += ' <i>' + article_dict[sorted_key]['journal'] + '</i>, ' + article_dict[sorted_key][
                'volume']
            if 'number' in article_dict[sorted_key]:
                content_to_be_written += ':' + article_dict[sorted_key]['number']
            if 'page' in article_dict[sorted_key]:
                content_to_be_written += ', pp. ' + article_dict[sorted_key]['page'].replace('--', '-')
            content_to_be_written += ', ' + article_dict[sorted_key]['year'] + '. '
            if 'doi' in article_dict[sorted_key]:
                content_to_be_written += f"<a href=\"https://doi.org/{article_dict[sorted_key]['doi']}\">link</a> "
            content_to_be_written += '<br>\n'
        a = article_dict[sorted_key]['year']
        my_index += 1
    content_to_be_written += html_ending_tag
    handle_file = open('out.html', 'w')
    handle_file.write(content_to_be_written)
    handle_file.flush()
    handle_file.close()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
