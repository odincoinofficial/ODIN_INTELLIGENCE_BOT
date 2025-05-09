from fpdf import FPDF

class OSINTReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "ODIN INTELLIGENCE REPORT", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, content)
        self.ln(5)

def generate_pdf_report(query, email, ip, domain, user):
    pdf = OSINTReport()
    pdf.add_page()
    pdf.add_section("Target", query)
    pdf.add_section("Email Info", email)
    pdf.add_section("IP Info", ip)
    pdf.add_section("Domain Info", domain)
    pdf.add_section("Username Info", user)

    filename = f"{query.replace('@', '_')}_report.pdf"
    pdf.output(filename)
    return filename