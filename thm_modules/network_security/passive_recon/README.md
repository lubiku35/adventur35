
# Passive Reconnaissance

Reconnaissance (recon) can be defined as a preliminary survey to gather information about a target. It is the first step in The Unified Kill Chain to gain an initial foothold on a system.

In passive reconnaissance, you rely on publicly available knowledge. It is the knowledge that you can access from publicly available resources without directly engaging with the target. 


> `whois` to query WHOIS servers  

> `nslookup` to query DNS servers  

> `dig` to query DNS servers  


These two online services allow us to collect information about our target without directly connecting to it.

- [https://www.shodan.io/](https://www.shodan.io/)

- [https://dnsdumpster.com/](https://dnsdumpster.com/)



## Passive Reconnaissance Activities

- Looking up DNS records of a domain from a public DNS server.

- Checking job ads related to the target website.

- Reading news articles about the target company.

## whois

- Registrar: Via which registrar was the domain name registered?

- Contact info of registrant: Name, organization, address, phone, among other things. (unless made hidden via a privacy service)

- Creation, update, and expiration dates: When was the domain name first registered? When was it last updated? And when does it need to be renewed?

- Name Server: Which server to ask to resolve the domain name?

## nslookup

| **Query** | **Result**         |
|:---------:|:------------------:|
| **A**     | IPv4 Addresses     |
| **AAAA**  | IPv6 Addresses     |
| **CNAME** | Canonical Name     |
| **MX**    | Mail Servers       |
| **SOA**   | Start of Authority |
| **TXT**   | TXT Records        |

`nslookup -type=$Query $IP/DOMAIN`

## dig 

**dig** - Domain Information Groper

`dig $IP/DOMAIN $QUERY`

