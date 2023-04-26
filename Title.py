# string="Hey its me bitch"
# print(string.title())

def format_name(f_name,l_name):

    #### Doc string

    
    """Take a first and last name and format
    it to return the title case version."""
    if f_name=="" or l_name=="":
        return "You didnt provide inputs"
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"Result:{formatted_f_name} {formatted_l_name}"
print(format_name("tridib","ghosh"))

