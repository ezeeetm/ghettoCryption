# ghettoCryption

This was made as a joke/proof of concept after we rec'd the email below:

> Hi, This is Haq khokhar, I am website Security Researcher and i have found some Security Vulnerability(BUG) in your website and it can cause damage your website  so may i report here ? there is any Appreciation reward/bug bounty program for valid report/bug ?

> Kindly response as soon as possible .

> Let me know how to Share the Vulnerability report ?

It was clear they had scraped our company's contact info in the html on our corporate website.  Our CTO quickly hexed out that address to prevent it in the future, and we joked that there should be a web service that does on-the-fly obfuscation in a similar fashion.  So, I made it.

It is meant to be hosted as an AWS Lambda function behind an AWS API Gateway.  Call it in a browser with /domain as the last url resource, and it will return the entire www.domain.com web page content obfuscated in hex and rendered in the browser in .js  
