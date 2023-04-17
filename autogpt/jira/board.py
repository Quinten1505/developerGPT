from jira import JIRA

def get_jira_ticket(jira_url, username, password, ticket_id):
    """
    Get JIRA ticket details.

    Args:
        jira_url (str): The JIRA instance URL.
        username (str): The JIRA username.
        password (str): The JIRA password or API token.
        ticket_id (str): The JIRA ticket ID (e.g., 'PROJECT-123').

    Returns:
        dict: A dictionary containing the JIRA ticket details.
    """
    # Authenticate and create a JIRA instance
    jira = JIRA(jira_url, basic_auth=(username, password))

    # Get the JIRA ticket
    ticket = jira.issue(ticket_id)

    # Extract ticket details
    ticket_details = {
        'id': ticket.key,
        'summary': ticket.fields.summary,
        'description': ticket.fields.description,
        'status': ticket.fields.status.name,
        'assignee': ticket.fields.assignee.displayName if ticket.fields.assignee else None
    }

    return ticket_details
