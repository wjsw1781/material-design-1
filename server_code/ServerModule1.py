import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.http_endpoint('/pdf_diff',methods=["GET","POST"])
def pdf_diff(**kw):
    return kw
    

@anvil.server.route("/get_pdf_diff")
def serve_my_page(**p):
    # This assumes there is a form called MyPageForm in your app:
    return anvil.server.FormResponse('MyPageForm',**p)

