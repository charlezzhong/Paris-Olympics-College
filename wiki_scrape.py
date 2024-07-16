import wikipediaapi

def fetch_infobox_vcard(name):
    wiki_wiki = wikipediaapi.Wikipedia('en', user_agent='wikipediaapi')
    page = wiki_wiki.page(name)

    if page.exists():
        return page.text
    else:
        print(f"Page for {name} does not exist.")
        return None

def extract_infobox_data(page_text):
    # Look for infobox template
    start_template = '{{Infobox'
    end_template = '\n}}'

    start_idx = page_text.find(start_template)
    if start_idx == -1:
        return "No Infobox found."

    end_idx = page_text.find(end_template, start_idx)
    if end_idx == -1:
        return "No end of Infobox found."

    infobox_content = page_text[start_idx:end_idx+len(end_template)]
    return infobox_content

# Example usage
athlete_name = "Simone Biles"
page_text = fetch_infobox_vcard(athlete_name)
if page_text:
    print(f"Infobox vcard content for {athlete_name}:")
    print(extract_infobox_data(page_text))