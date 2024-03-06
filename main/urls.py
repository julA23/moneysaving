from django.urls import path
from main.views import dashboard, create_transaction, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_transaction, remove_transaction, get_transaction_json_today, add_transaction_ajax, get_transaction_json_tomorrow, get_transaction_json_yesterday, format_last_login, format_today, financial_report, get_transaction_json_expenses, get_transaction_json_income, get_transaction_json_transfer, get_transaction_json_all

app_name = 'main'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create-transaction', create_transaction, name='create_transaction'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-transaction/<int:id>', edit_transaction, name='edit_transaction'),
    path('remove/<int:id>', remove_transaction, name='remove_transaction'),
    path('get-transaction/', get_transaction_json_today, name='get_transaction_json_today'),
    path('add-transaction-ajax/', add_transaction_ajax, name='add_transaction_ajax'),
    path('get-transaction-tomorrow/', get_transaction_json_tomorrow, name='get_transaction_json_tomorrow'),
    path('get-transaction-yesterday/', get_transaction_json_yesterday, name='get_transaction_json_yesterday'),
    path('format-last-login/', format_last_login, name='format_last_login'),
    path('format-today/', format_today, name='format_today'),
    path('financial-report/', financial_report, name='financial_report'),
    path('get_transaction-json-expenses/', get_transaction_json_expenses, name='get_transaction_json_expenses'),
    path('get-transaction-json-income/', get_transaction_json_income, name='get_transaction_json_income'),
    path('get-transaction-json-transfer/', get_transaction_json_transfer, name='get_transaction_json_transfer'),
    path('get-transaction-json-all/', get_transaction_json_all, name='get_transaction_json_all'),

]