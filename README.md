# Startup-Sucess-Index-Simulator


# Purpose

This project shows off a simulation of a Europe based seed funded startup and it's success factor with two variable inputs, amount of money given to the startup and the corruption index of the specific European country the startup is located in.

<hr>

**Example run**

The simulation unfolded across an expansive canvas, conducting a remarkable 10,000 iterations. Each iteration featured a dynamic assembly of 100 startups, culminating in an impressive aggregate of 1 million startups. This extensive exploration provided an unparalleled depth of insight, vividly illustrated through graphs portraying the performance metrics of the top 10, bottom 10, and all European countries in the domain of successful startup endeavors.

In the intricate dance of each simulation run, the generation of seed fundings followed a nuanced process dictated by a normal distribution. This method injected realism and diversity into the financial landscapes of the startups under scrutiny. Introducing a critical dimension, the corruption index, tailored for each country, played a pivotal role in shaping outcomes. This corruption parameter added a layer of complexity to the analyses, significantly influencing the simulation results. The incorporation of the corruption index ensures a robust and realistic portrayal of the challenges and dynamics in the realm of startup success across diverse European landscapes.

<hr>

**Inputs for the example run:**

NUM_SIMULATIONS - Number of simulations, which is 10,000
STARTUP_COUNT - Number of start-up firms, which is 100
CPI_WEIGHT - Importance of CPI (Consumer Price Index) during calculation
SEED_FUNDING_MEAN - Average value of seed funding, i.e., the amount of money
SEED_FUNDING_STD_DEV - Standard deviation from the average funding
SEED_FUNDING_WEIGHT - Importance of average funding during calculation

<hr>

**Example run plots:**

**All**
![image](https://github.com/HarisKordic/Startup-Success-Index-Simulator/assets/58373221/847cc384-92ae-43d5-8650-e5cd881bfd2f)

**Bottom 10**
![image](https://github.com/HarisKordic/Startup-Success-Index-Simulator/assets/58373221/f4b9dcfd-ca51-4a43-b895-920e2ce18f48)

**Top 10**
![image](https://github.com/HarisKordic/Startup-Success-Index-Simulator/assets/58373221/ae7f16cc-2f67-433c-a897-237d0889d8bf)



