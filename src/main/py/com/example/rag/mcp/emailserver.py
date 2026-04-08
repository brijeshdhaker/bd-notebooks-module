#
# python src/main/py/com/example/rag/mcp/emailserver.py
#
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from email.message import EmailMessage
from com.example.utils.GmailProcessor import GmailProcessor

# 1. Initialize FastMCP server
mcp = FastMCP("Email Notification MCP Server")

# 2. Define Complex Data Type for Email
class EmailPayload(BaseModel):
    recipient: EmailStr
    subject: str
    body: str
    cc: Optional[List[EmailStr]] = Field(default=None, description="Optional CC list")
    attachment_names: Optional[List[str]] = Field(default=None, description="List of attachment filenames")


# 1. Define a complex data structure
class UserProfile(BaseModel):
    user_id: int
    tags: list[str] = Field(description="A list of interests")
    metadata: dict[str, str] = Field(description="Key-value pairs for settings")

GmailProcessor()

# 3. Define Tool with Complex Input
@mcp.tool()
def send_email(email: EmailPayload) -> str:
    """_summary_
    Sends a complex, structured email with CC and attachment metadata.
    """
    msg = EmailMessage()
    msg['From'] = "brijeshdhaker@gmail.com"
    msg['To'] = email.recipient
    msg['Subject'] = email.subject
    msg.set_content(email.body)

    if email.cc:
        msg['Cc'] = ", ".join(email.cc)
        
    # Simulated Attachment Handling
    if email.attachment_names:
        return f"Drafted email to {email.recipient} with {len(email.attachment_names)} attachments: {email.attachment_names}"

    # --- SMTP Logic Here (e.g., using smtplib) ---
    return GmailProcessor.send(msg)

#
if __name__ == "__main__":
    mcp.run(transport="stdio")