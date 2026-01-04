
## Course Information
- **Course type:** Practical lecture / lab
- **Duration:** 90 minutes (1.5 hours)
- **Format:** Hands-on with guided exercises
- **Target audience:** University students with basic programming knowledge
- **Prerequisites:** Basic understanding of JSON and HTTP

---

## Learning Objectives
By the end of this session, students will be able to:
- Explain the purpose and core concepts of workflow automation
- Describe the main components of n8n (workflows, nodes, triggers, executions)
- Build and debug simple automation workflows
- Implement a webhook-driven workflow with conditional logic
- Critically reflect on the benefits and limits of low-code automation tools

---

## Required Preparation

### Software
- n8n (cloud account or local Docker installation)
- Modern web browser

### Prior Knowledge
- Basic programming concepts
- JSON data structures
- HTTP request/response basics

---

## Teaching Notes
- Emphasize data flow over line-by-line execution
- Encourage experimentation and failure during exercises
- Focus on conceptual understanding rather than tool-specific details

---


## Subgoal Overview and Teaching Plan

| Subgoal | Taught Subject Matter | Learning Goal | Start (min) | End (min) | Material Needed (Teacher) |
|--------|-----------------------|---------------|-------------|-----------|----------------------------|
| 1. Motivation & Context | Workflow automation concepts; examples from academia and industry; positioning of n8n | Students understand *why* automation is relevant and can name suitable application scenarios | 0 | 10 | Slides with motivation examples; short real-world use cases; discussion prompt |
| 2. Core Concepts of n8n | Workflows, nodes, triggers, data flow (JSON), executions, debugging | Students can explain the basic mental model of n8n and its core components | 10 | 20 | Slides with diagrams; live n8n instance; example workflow for demonstration |
| 3. First Guided Workflow | Manual Trigger, Set node, Function node, execution inspection | Students can create and run a simple workflow and inspect its data flow | 20 | 35 | Prepared demo workflow; step-by-step checklist; working n8n environment |
| 4. Independent Hands-on Exercise | Webhook Trigger, IF node, HTTP Request node, validation logic | Students can independently build a webhook-based workflow with conditional logic | 35 | 55 | Exercise sheet; sample JSON payloads; mock API endpoint (e.g., httpbin); fallback solution |
| 5. Debugging & Error Handling | Execution logs, common errors, pinned data, debugging strategies | Students can diagnose and fix typical workflow errors | 55 | 65 | Intentionally broken workflows; debugging examples; checklist of common mistakes |
| 6. Advanced Use & Outlook | API integration, AI/LLM-based nodes, conditional routing, ethical aspects | Students gain awareness of advanced use cases and limitations of automation tools | 65 | 80 | Demo workflow (AI or API-based); slides on ethics, privacy, and costs |
| 7. Reflection & Wrap-up | Critical reflection, transfer to own context, outlook | Students can critically assess when and how n8n should be used | 80 | 90 | Reflection questions; summary slide; optional assignment description |


## Schedule & Content

### Motivation and Context

- What is workflow automation?
- Typical automation scenarios in academia and industry
- Positioning n8n among other tools (scripts, Zapier, Make)
- Short discussion: “Which task would you automate?”

---

### 10–20 min — Core Concepts of n8n
- Workflows as directed data-flow graphs
- Trigger nodes vs. regular nodes
- Data model: JSON in / JSON out
- Executions, logs, and debugging
- Tour of the n8n editor interface

---

### 20–35 min — Guided First Workflow
- Creating a new workflow
- Manual Trigger node
- Set node: defining structured data
- Function node: basic data transformation
- Running and inspecting an execution
- Mini exercise: add name and timestamp to the output

---

### 35–55 min — Student Hands-on Exercise
**Task:** Build a webhook-based workflow
- Webhook Trigger: receiving JSON data
- IF node: validating incoming data
- Set or Function node: preparing output
- HTTP Request node: forwarding accepted data
- Handling rejected requests
- Testing the workflow with sample payloads

---

### 55–65 min — Debugging and Discussion
- Common beginner mistakes
- Reading execution data
- Using pinned data for testing
- Group discussion of encountered issues

---

### 65–80 min — Advanced Example and Outlook
- Demonstration: API-based data enrichment
- Example: AI-powered text classification or summarization
- Conditional routing based on AI output
- Discussion: costs, privacy, reproducibility, ethics

---

### 80–90 min — Reflection and Wrap-up
- When is automation not the right solution?
- Strengths and limitations of low-code tools
- Use cases in study projects and theses
- Outlook to further topics (deployment, security, scaling)

---

## Optional Follow-up Assignment
- Identify a real-world task suitable for automation
- Design and implement a simple n8n workflow
- Document the workflow logic and reflection in a short report

---
