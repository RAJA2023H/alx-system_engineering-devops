<h1 align="center">POSTMORTEM: WEB APPLICATION OUTAGE ON AUGUST 15, 2024</h1>	    

<h2 align="left"> Issue Summary</h2>

<h3 align="left">Duration:</h3> August 15, 2024, 14:00 - 16:30 GMT (2 hours, 30 minutes)

<h3 align="left">Impact:</h3> 45% of users experienced slow response times or were unable to access the web application, resulting in a significant drop in traffic and user engagement. The issue primarily affected users in Europe and North America.

<h3 align="left">Root Cause:</h3> A misconfigured load balancer that caused an uneven distribution of traffic, leading to server overload and degraded application performance.

<h2 align="left">Timeline</h2>

14:00 GMT - Issue detected by monitoring alerts indicating increased server response times and error rates.

14:05 GMT - On-call engineer began investigating the issue, initially suspecting a database bottleneck due to recent schema changes.

14:20 GMT - Database queries were analyzed, and indexes were checked; no anomalies found. Assumption made that the issue might be related to recent code deployment.

14:40 GMT - Rollback of the latest deployment was initiated, but the issue persisted, indicating the problem was not code-related.

15:00 GMT - Network team was brought in to investigate potential connectivity issues.

15:20 GMT - Load balancer configuration was reviewed, revealing an incorrect routing rule that was sending most traffic to a single server node.

15:30 GMT - Configuration was corrected, redistributing traffic evenly across all server nodes.

16:00 GMT - System performance began to stabilize; monitoring showed a decrease in response times and errors.

16:30 GMT - All services confirmed to be fully operational. Post-incident review commenced.

<h2 align="left">Root Cause and Resolution</h2>

<h3 align="left">Root Cause:</h3>
The root cause was a misconfiguration in the load balancer settings. A routing rule was incorrectly set during a recent update, which led to most incoming traffic being directed to a single server node.
This server became overwhelmed, leading to high response times and frequent errors for users attempting to access the web application.
The load balancer was not properly distributing traffic across the available servers, which resulted in the degradation of service.

<h3 align="left">Resolution:</h3>
Once the issue was identified, the load balancer configuration was corrected to ensure even traffic distribution across all server nodes.
This involved modifying the routing rules and validating the changes to confirm proper load balancing.
After the fix, server performance was closely monitored to ensure the system returned to normal operation. Full service was restored,
and no further issues were detected.

<h2 align="left">Corrective and Preventative Measures</h2>

<h3 align="left">Improvements and Fixes:</h3>

Implement stricter validation checks during load balancer configuration updates.

Enhance monitoring to include alerts for uneven traffic distribution across server nodes.

Improve documentation and training for engineers responsible for load balancer management.


<h2 align="left">TODO List:</h2>

- Task 1: Patch the load balancer to include an automated check that verifies traffic distribution post-configuration changes.

- Task 2: Add specific monitoring for server node load to quickly detect any imbalance in traffic distribution.

- Task 3: Conduct a training session for the engineering team on best practices for load balancer management.

- Task 4: Review and update the incident response plan to include a faster escalation process for issues involving load balancer configurations.
