import json

from jsonpickle import encode as jsonpickle_encode

from adapters.interfaces.api.handle import API
from adapters.interfaces.web.templates import (
    temp_index_html,
    temp_form_html,
    temp_form_error_html,
    temp_result_html,
    temp_list_html,
    temp_li_html
)

from application.transaction import (
    get_content_file,
    process_transaction,
    list_transaction
)

app = API()

# =============================================================
# routers for web
@app.route("/")
def home(request: any, response: any) -> None:
    """This function renders template home."""
    response.content_type = "text/html"
    response.text = temp_index_html

@app.route("/web/form")
def web_form(request: any, response: any) -> None:
    """This function renders form."""
    response.content_type = "text/html"
    response.text = temp_form_html

@app.route("/web/upload")
def web_upload(request: any, response: any) -> None:
    """This function renders process file."""
    response.content_type = "text/html"

    block = get_content_file(request.body)
    if block == "":
        response.text = temp_form_error_html
        return

    process_transaction(block)
    response.text = temp_result_html

@app.route("/web/list")
def web_list(request: any, response: any) -> None:
    """This function renders list transactions home."""
    td_li_html = ""

    for item in list_transaction():
        td_li_html += temp_li_html.format(
            transaction=item
        )

    response.content_type = "text/html"
    response.text = temp_list_html.format(
        backgroundstyle="{background-color: #dddddd;}",
        rg_li_html=td_li_html
    )


# =============================================================
# routers for api
@app.route("/api/upload")
def upload(request: any, response: any) -> None:
    """This function process file."""
    response.content_type = "application/json"

    if request.method != "POST":
        response.text = json.dumps({"error": "not allowed method"})
        return

    block = get_content_file(request.body)
    if block == "":
        response.text = json.dumps({"error": "unrecognized file"})
        return

    process_transaction(block)
    response.text = json.dumps({"message": "processed file"})


@app.route("/api/list")
def list_transactions(request: any, response: any) -> None:
    """This function list transaction."""
    response.content_type = "application/json"

    if request.method != "GET":
        response.text = json.dumps({"error": "not allowed method"})
        return

    transactions = list_transaction()
    response.text = jsonpickle_encode(transactions, unpicklable=False)
