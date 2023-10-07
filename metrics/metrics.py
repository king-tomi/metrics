"""
Module for computing different metrics

Date: 04-09-2023
"""


def ca(Na: int, Np: int) -> float:
    """
    calculates the Configuration/Abortion Rate
    
    params:

        Na -> int: Number of aborted configuration processes

        Np -> int: Number of logins (started configurations)

    returns:
        The ratio of the aborted processes to login
    """
    return round(Na / Np, 3)

def rtr(Rp: int, Dp: int) -> float:
    """
    calculates the rate of return of products after they have been delivered

    params:

        Rp -> int: Number of returned products

        Dp -> int: Number of delivered products

    returns:
        The rate of return
    """
    return round(Rp / Dp, 3)

def cr(Noc: int, Nolc: int, Nonc: int) -> float:
    """
    Calculates and show the relationship between new customers and lost customers at a given period T

    params:

        Noc -> int: Number of customers

        Nolc -> int: Number of lost customers

        Nonc -> int: Number of new customers

    returns:
        The churn rate for new customers at a given period T
    """
    return round(Nolc / (Noc + Nonc - Nolc), 3)

def rr(Rec: int, Nc: int) -> float:
    """
    calculates and shows how frequently buyers make repurchases on same products after first purchase

    params:

        Rec -> int: Number of repurchase through existing customers

        Nc -> int: Number of new customers

    returns:
        the rate of repurchase
    """
    return round(Rec / Nc, 3)

def cor(Co: int, Nd: int) -> float:
    """
    calculates and show how frequent customers critic products that have been bought and delivered

    params:

        Co -> int: Number of complaints

        Nd -> int: Number of deliveries

    returns:
        The rate of complaints/criticisms given
    """
    return round(Co / Nd, 3)

def socr(Nos: int, Npo: int) -> float:
    """
    calculates and shows the rate of cancellation made by sellers on placed orders

    params:

        Nos -> int: Number of orders cancelled by sellers

        Npo -> int: Number of placed order

    returns:
        The rate of cancellation
    """
    return round(Nos / Npo, 3)

def socrap(Ncs: int, Npo: int) -> float:
    """
    calculates and shows the rate of change made by sellers on placed orders

    params:

        Ncs -> int: Number of orders changed by sellers

        Npo -> int: Number of placed order

    returns:
        The rate of change of placed orders
    """
    return round(Ncs / Npo, 3)

def cocr(Noc: int, Npo: int) -> float:
    """
    calculates and shows the rate of cancellation made by customers on placed orders

    params:

        Noc -> int: Number of orders cancelled by customers

        Npo -> int: Number of placed order

    returns:
        The rate of cancellation made by customer
    """
    return round(Noc / Npo, 3)

def socrap(Ncc: int, Npo: int) -> float:
    """
    calculates and shows the rate of change made by customers on placed orders

    params:

        Ncc -> int: Number of orders changed by customers

        Npo -> int: Number of placed order

    returns:
        The rate of change of placed orders
    """
    return round(Ncc / Npo, 3)

def csr(Nsc: int, Nstc: int) -> float:
    """
    calculates and shows the most configuration results

    params:

        Nsc -> int: Number of sold configuration

        Nstc -> int: Number of started configuratio

    returns:
        The rate of configuration made
    """
    return round(Nsc / Nstc, 3)

def assp(Tsi: int, Tmc: int) -> int:
    """
    calculates the difference between income made from sales and manufacturing cost
    Used to know how lucrative a product is

    params:

        Tsi -> int: Total sales income

        Tmc -> int: Total manufacturing cost

    returns:
        Difference between income sales and cost
    """
    return Tsi - Tmc

def pc(Cp: int, Tp: int) -> float:
    """
    Measures the relationship between common parts and total parts

    params:

        Cp -> int: Number of common parts

        Tp -> int: Total Number of parts

    returns:
        The rate of common parts in total parts
    """
    return round(Cp / Tp, 3)

def dpi(Vi: list, Vn: int, n: int, Di: int, Ai: list) -> float:
    """
    Guages how far along in the production process variation generation is

    params:

        Vi -> list: list of difference existing in process i

        Vn -> int: final number of varieties offered

        n -> int: number of processes

        Di -> int: average throughput time from beginning production of sale

        Ai -> list: Added at process i

    returns:
        rate of variation
    """
    if len(Vi) > n and len(Vn) > n: #check if recorded variations are lesser than the number of processes
        return -1
    
    if len(Vi) != len(Di) and len(Vi) != len(Ai): #checks if all values recorded at process i are the same length
        return -1
    
    numerator = sum([ Di * v * a for v,a in list(zip(Vi,Ai)) ])
    denominator = n * Vn * Di * sum(Ai)

    return round(numerator / denominator, 3)

def si(v: list, n: int, Ci: list, Cj: list) -> float:
    """
    Shows the contribution of setup expenses to total manufacturing cost

    params:

        v: number of difference existing in process i

        n: number of processes

        Ci: cost of setup at process i

        Cj: total cost of product jth

    returns:
        expenses contribution rate
    """
    if len(Ci) > n and len(Cj) > n and len(v) > n: #check if recorded variations are lesser than the number of processes
        return -1
    
    return round(sum([ v * c for v,c in list(zip(v, Ci) )]) / sum(Cj), 3)

def qor(Tdoz: int, Tdo: int) -> float:
    """
    Measures production efficiency

    params:

        Tdoz: Number of delivered on time orders with zero defects

        Tdo: Total Number of orders

    returns:
        rate of efficiency
    """
    return round(Tdoz / Tdo, 3)

def pfp(Tsip: int, Tmcp: int) -> int:
    """
    calculates the difference between income made from sales and manufacturing cost
    Used to know how lucrative a product is

    params:

        Tsi -> int: Total sales income for product family

        Tmc -> int: Total manufacturing cost for produc family

    returns:
        Difference between income sales and cost for a product family
    """
    return Tsip - Tmcp

def uv(Npv: int, Nppv: int) -> float:
    """
    Measures how well the solution space is utilized by customers

    params:

        Npv -> int: Number of perceived variants

        Nppv -> int: Number of all possible variants

    returns:
        The rate of space solution utilization
    """
    return round(Npv / Nppv , 3)

def rpr(Nr: int, Np: int) -> float:
    """
    calculates and shows how frequently buyers make repurchases on same products or come back for different product

    params:

        Nr -> int: Number of repurchases

        Np -> int: Number of purchases

    returns:
        the rate of repurchase
    """
    return round(Nr / Np, 3)

def car(Nac: int, Nic: int) -> float:
    """
    calculates the Configuration/Abortion Rate by customers
    
    params:

        Nac -> int: Number of aborted configuration processes

        Nic -> int: Number of initiated configurations

    returns:
        The ratio of the aborted processes to initiated cofigurations
    """
    return round(Nac / Nic, 3) 

def mu(NV: int, KM: int) -> float:
    """
    Measures the number of modules needed to generate variants present in the solution space

    params:

        NV -> int: Number of product variants required by customers

        KM -> int: Number of different module required to build all variants in the product portfolio

    returns:
        The rate of required modules needed to generate solution space variant
    """
    return round(NV / KM, 3)

def mcm(Ncm: int, Ndm: int) -> float:
    """
    Calculates the ratio of number of common modules to the total number of different modules present

    params:

        Ncm -> int: Number of different modules

        Ndm -> int: Total number of different modules

    returns:
        The rate of variation
    """
    return round(Ncm / Ndm, 3)

def nmp(m: list, n: int) -> float:
    """
    Measures the typical quantity of modules produced using various manufacturing processes

    params:

        m -> list: number of different modules manufactured at a given process i

        n -> int: number of different processes

    returns:
        Rate of modules produced using different manufacturing processes
    """
    if len(m) > n:
        return -1
    
    return round(sum(m) / n)

def dml(Tlc: list, Tmc: list, n: int) -> float:
    """
    Measures process robustness

    params:

        Tlc -> list: Labor cost of manufactring product i

        Tmc -> list: Total cost of manufacturing product i

        n -> int: number of different products

    returns:
        Ratio of process robustness
    """
    if len(Tlc) > n and len(Tmc) > n:
        return -1
    
    return round(sum([ x / y for x,y in list(zip(Tlc, Tmc))]) / n, 3)

def pvi(p: list, n: int) -> float:
    """
    Measures the diversity of process expansion based on the introduction of a new product option

    params:

        p -> list: number of processes introduced for product i

        n -> int: number of new product options in the period

    returns:
        The rate of process expansion
    """
    if len(p) > n:
        return -1
    
    return sum(p) / n