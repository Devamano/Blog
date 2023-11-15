# Import necessary libraries
import streamlit as st
from PIL import Image

# Set page title
st.title("  Lehman Brothers: A Chronicle of Financial Grandeur and Tragic Demise")

# Add an introductory paragraph
st.write("""  Lehman Brothers, a name synonymous with financial prowess and innovation, stood as a titan 
            among investment banks, whose influence extended across the global financial landscape.However, the 
            company's meteoric rise was tragically cut short by a series of missteps and the tumultuous events of the 
            2008 financial crisis. With assets valued at a staggering $691 billion, Lehman's collapse marked one of 
            the most significant bankruptcies in American history, sending shockwaves through the financial world 
            and leaving an indelible mark on the global economy. 
            Who are  Lehman brothers? How did a company with such huge reputation that prospered 
            decades come to an end ?.  We could find answers to these questions that arise once on completion of this case. 
""")

# Write a paragraph about the first image
st.header("  Who are Lehman brothers?")
st.write("""   It was one of the global investment bank offering wide range of financial services like investment 
            banking, brokerage and asset management.It was initially started as a general Store at Alabama  ,
            Germany  by Henry, Immanuel and mayer lehman. Initially Farmers paid for goods in cotton which 
            eventually let them to develop as a cotton Trade centre later as he has passed the diversified themselves 
            into commodities trading and brokerage services and grew into an international power house. Here's a 
            time line depicting it's growth """)

image1_path1 = r"blog/Picture 2.jpg"
image1 = Image.open(image1_path1)
st.image(image1, caption="Image 1: A Brief History of Lehman Brothers Fig:1.1" )

# Write a paragraph about the second image
st.write("""While Lehman Brothers' net worth fluctuated significantly over its history, it is difficult to provide precise 
            figures for each year due to the limitations of historical financial data and the varying methodologies used 
            to calculate net worth. However, available information suggests that the firm's net worth generally 
            trended upward throughout its existence, with some notable periods of growth and decline. It can be 
            depicted as below.""")
# Insert the second image
image1_path2 = r"blog/Picture1.jpg"
image2 = Image.open(image1_path2)
st.image(image2, caption="Image 2: Lehmen Brothers Net worth over years Fig 1.2", use_column_width=True)


st.header(" How did a company with such reputation have a catastrophic end?")
# Write additional content
st.write("""     The early 2000s witnessed the rise of the subprime mortgage market, a sector that offered high returns
             but also carried significant risks.Enticed by the promise of high returns, Lehman Brothers invested 
             heavily in subprime mortgages, believing that they would continue to generate hefty profits.However, 
             their euphoria on subprime mortgages was short-lived. As the housing market began to falter in 2007, 
             homeowners with subprime mortgages found themselves unable to repay their loans. The value of MBS 
             plummeted, leaving Lehman Brothers with a mountain of toxic assets. The firm's attempt to offload the 
             assets became futile.
             Correspondingly Lehman Brothers used complex financial instruments, such as collateralized debt 
             obligations (CDOs), to manage its risk. However, these instruments were difficult to understand and 
             value, and they exacerbated Lehman Brothers' losses when the subprime mortgage market collapsed.
             They failed to adequately manage their  risk. The company's executives were overly confident in their 
             ability to weather the subprime mortgage crisis, and they did not take sufficient steps to protect the 
             company from the fallout.
              On September 15, 2008 the firm filed its bankruptcy sending shock waves to the global financial system. 
              It marked the largest bankruptcy in the U.S at that time. Millions of investors lost their investment 
              across the world. 
              The collapse of the housing market led to widespread foreclosures and job losses, while the global 
              economy plunged into a deep recession.
              """)
st.header(" Conclusion")
st.write("""     The story of Lehman brothers serves as a remainder for the risks inherent in excessive risk taking and 
            mismanaged financial strategies. It is a cautionary tale that provides insights and prompting reassurance 
            of the financial regulations,transparency  and a sound risk management.""")

