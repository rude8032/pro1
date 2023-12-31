import matplotlib.pyplot as plt
import networkx as nx
import os

# Directory to save images
save_directory = "./"

def draw_flowchart(flow, title, filename):
    G = nx.DiGraph()
    for node, edges in flow.items():
        for edge in edges:
            G.add_edge(node, edge)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', arrows=True)
    plt.title(title)
    
    # Save the figure with the given filename
    plt.savefig(filename)
    
    # Show the plot (optional)
    plt.show()
    

# Sales Flowchart
flow_sales = {
    "Start Sales": ["Create Invoice", "View Sales Report", "Manage Customers"],
    "Create Invoice": ["Send Invoice", "Update Invoice Status"],
    "View Sales Report": ["Filter by Date", "Export Report"],
    "Manage Customers": ["Add Customer", "Update Customer Details"]
}

# Purchases Flowchart
flow_purchases = {
    "Start Purchases": ["Create Purchase Order", "View Purchase History", "Manage Suppliers"],
    "Create Purchase Order": ["Send Order", "Track Order Status"],
    "View Purchase History": ["Filter by Date", "Export History"],
    "Manage Suppliers": ["Add Supplier", "Update Supplier Details"]
}



# e-Waybill Flowchart
flow_ewaybill = {
    "Start e-Waybill": ["Generate e-Waybill", "View e-Waybill Status", "Update e-Waybill Details"],
    "Generate e-Waybill": ["Send e-Waybill", "Print e-Waybill"],
    "View e-Waybill Status": ["Filter by Date", "Track e-Waybill"],
    "Update e-Waybill Details": ["Modify Details", "Cancel e-Waybill"]
}

# Inventory Flowchart
flow_inventory = {
    "Start Inventory": ["Add Product", "View Inventory Levels", "Manage Suppliers"],
    "Add Product": ["Set Product Details", "Update Stock Levels"],
    "View Inventory Levels": ["Filter by Category", "Generate Inventory Report"],
    "Manage Suppliers": ["Add Supplier", "Update Supplier Details"]
}



# Ledger Flowchart
flow_ledger = {
    "Start Ledger": ["View Transactions", "Add Transaction", "Manage Accounts"],
    "View Transactions": ["Filter by Date", "Generate Ledger Report"],
    "Add Transaction": ["Record Income", "Record Expense"],
    "Manage Accounts": ["Add Account", "Update Account Details"]
}

# Expense Flowchart
flow_expense = {
    "Start Expense": ["Add Expense", "View Expenses", "Manage Categories"],
    "Add Expense": ["Record Expense Details", "Attach Receipt"],
    "View Expenses": ["Filter by Date", "Generate Expense Report"],
    "Manage Categories": ["Add Category", "Update Category Details"]
}



# Masters Flowchart
flow_masters = {
    "Start Masters": ["Manage Users", "Manage Settings", "Manage Data Types"],
    "Manage Users": ["Add User", "Update User Details", "Delete User"],
    "Manage Settings": ["Update Application Settings", "Configure Preferences"],
    "Manage Data Types": ["Add Data Type", "Update Data Type Details", "Delete Data Type"]
}

# Reports Flowchart
flow_reports = {
    "Start Reports": ["Generate Sales Report", "View Inventory Report", "Access Financial Reports"],
    "Generate Sales Report": ["Filter by Date", "Export Report", "Print Report"],
    "View Inventory Report": ["Filter by Product", "Export Report", "Print Report"],
    "Access Financial Reports": ["View Profit and Loss Statement", "View Balance Sheet", "Generate Custom Report"]
}


# Manage Staff (New) Flowchart
flow_manage_staff = {
    "Start Manage Staff": ["Add Staff", "View Staff Details", "Update Staff Information"],
    "Add Staff": ["Enter Personal Details", "Set Permissions", "Assign Role"],
    "View Staff Details": ["Filter by Department", "Search by Name", "Export Details"],
    "Update Staff Information": ["Modify Personal Details", "Change Role", "Remove Staff"]
}

# Settings Flowchart
flow_settings = {
    "Start Settings": ["General Settings", "Security Settings", "Notification Settings"],
    "General Settings": ["Update Application Language", "Set Timezone", "Customize UI"],
    "Security Settings": ["Change Password", "Set Two-Factor Authentication", "Manage Permissions"],
    "Notification Settings": ["Configure Email Notifications", "Set Alert Preferences", "Manage Notification Channels"]
}


# Subscription Flowchart
flow_subscription = {
    "Start Subscription": ["Subscribe to Plan", "View Subscription Details", "Manage Payment Methods"],
    "Subscribe to Plan": ["Choose Plan", "Enter Payment Details", "Confirm Subscription"],
    "View Subscription Details": ["Check Plan Status", "Review Payment History", "Upgrade/Downgrade Plan"],
    "Manage Payment Methods": ["Add Payment Method", "Update Payment Details", "Remove Payment Method"]
}

# Contact Us Flowchart
flow_contact_us = {
    "Start Contact Us": ["Access Contact Information", "Submit Support Request", "View FAQs"],
    "Access Contact Information": ["Retrieve Phone Number", "Find Email Address", "Visit Physical Address"],
    "Submit Support Request": ["Describe Issue", "Attach Files", "Receive Ticket Number"],
    "View FAQs": ["Search for Questions", "Browse Categories", "Submit Feedback"]
}

# Logout Flowchart
flow_logout = {
    "Start Logout": ["Confirm Logout", "End Session", "Clear Session Data"],
    "Confirm Logout": ["Close Active Sessions", "Terminate Active Connections", "Logout from All Devices"],
    "End Session": ["Logout Confirmation", "Redirect to Login Page", "Clear Cookies"]
}



# Draw and save flowcharts
draw_flowchart(flow_sales, "Sales Functionality Flowchart", os.path.join(save_directory, "Sales_Functionality_Flowchart.png"))
draw_flowchart(flow_purchases, "Purchases Functionality Flowchart", os.path.join(save_directory, "Purchases_Functionality_Flowchart.png"))
draw_flowchart(flow_ewaybill, "e-Waybill Functionality Flowchart", os.path.join(save_directory, "e-Waybill_Functionality_Flowchart.png"))
draw_flowchart(flow_inventory, "Inventory Functionality Flowchart", os.path.join(save_directory, "Inventory_Functionality_Flowchart.png"))
draw_flowchart(flow_ledger, "Ledger Functionality Flowchart", os.path.join(save_directory, "Ledger_Functionality_Flowchart.png"))
draw_flowchart(flow_expense, "Expense Management Flowchart", os.path.join(save_directory, "Expense_Management_Flowchart.png"))
draw_flowchart(flow_masters, "Masters Functionality Flowchart", os.path.join(save_directory, "Masters_Functionality_Flowchart.png"))
draw_flowchart(flow_reports, "Reports Management Flowchart", os.path.join(save_directory, "Reports_Management_Flowchart.png"))
draw_flowchart(flow_manage_staff, "Manage Staff (New) Functionality Flowchart", os.path.join(save_directory, "Manage_Staff_New_Functionality_Flowchart.png"))
draw_flowchart(flow_settings, "Settings Management Flowchart", os.path.join(save_directory, "Settings_Management_Flowchart.png"))
draw_flowchart(flow_subscription, "Subscription Management Flowchart", os.path.join(save_directory, "Subscription_Management_Flowchart.png"))
draw_flowchart(flow_contact_us, "Contact Us Functionality Flowchart", os.path.join(save_directory, "Contact_Us_Functionality_Flowchart.png"))
draw_flowchart(flow_logout, "Logout and Session Management Flowchart", os.path.join(save_directory, "Logout_and_Session_Management_Flowchart.png"))