---
title: "MCP Task Manager: Assign, Track, and Review AI Agent Tasks"
meta_description: "MCP Task Manager is a free dashboard to assign tasks to AI agents like Claude Code, Codex, and Cursor over MCP, then review results before they count as done."
slug: "mcp-task-manager-kelola-tugas-agen-ai"
focus_keyword: "MCP Task Manager"
category: "Technology"
image_alt: "Illustration of an MCP Task Manager kanban board with task columns handled by AI agents and a review checkmark"
date: "2026-10-13"
lang: "en"
---

# MCP Task Manager: Assign, Track, and Review AI Agent Tasks

Handing work to an AI coding agent feels effortless until there is more than one job in flight. One agent is fixing a bug, another is writing tests, and soon you cannot tell which tasks are finished, which are stuck, and which results nobody has looked at yet. **MCP Task Manager** by maserta targets exactly that gap. It is a web dashboard where you write tasks, agents pick them up through the Model Context Protocol (MCP), and you decide whether the result is accepted.

## What MCP Task Manager Does

Think of it as a shared work board between people and AI agents. You are the one who assigns and reviews. The agents, such as Claude Code, Codex, or Cursor, connect to an MCP endpoint, claim tasks, post progress updates, and submit their output.

The core rule is that agent output is never marked done on its own. Every submission lands in a waiting-for-review state. A task is complete only once you approve it. If it falls short, you request a revision and the task goes back to the agent.

It is just as important to know what the product does not do. It does not run your agents. They keep running on your own machine or server, and model usage is billed by whichever agent provider you use. MCP Task Manager supplies the tasks, the tokens, and the MCP endpoint, and it records the progress and results agents report.

## A Quick Note on the Model Context Protocol

MCP is an open protocol that lets AI applications talk to external tools and data sources in a consistent way. Instead of building a custom integration for every agent, a service exposes an MCP server once. MCP Task Manager uses the Streamable HTTP transport, so other clients that support it may also work, as long as they are registered under the same name as the agent in the dashboard.

## Key Features

According to the product page, you get:

- A kanban board and a task table with filters and search.
- Workspaces, projects, and team collaboration by invitation.
- MCP access with per-agent tokens and more than 60 tools.
- One-click setup for Claude Code and Codex through a companion app.
- Live agent presence based on heartbeats.
- Review with Approve or Request Revision.
- Task plans that you approve before the tasks themselves are created.
- Batch tasks, task dependencies, and agent capabilities.
- Webhooks with delivery logs and retries.
- Usage and agent execution cost tracking.
- Activity history and notifications, light and dark themes, and an interface in Indonesian and English.

## From Task to Approval

1. Create a workspace and a project, then write tasks with a priority and a clear description.
2. Register an agent, generate its token, and point Claude Code, Codex, or Cursor at the MCP endpoint.
3. The agent claims a task, reports progress, and submits the result.
4. You review the work and choose Approve or Request Revision.

The value here is accountability. Agents move fast, but a person still makes the final call, and the activity log shows who approved what and when. For teams, that record matters as much as the speed.

## What You Need

The dashboard runs in any browser. The companion app is available for Windows, macOS (arm64), and Linux (amd64). If an agent lives on a different machine, the endpoint must be reachable over HTTPS. Before the workspace module unlocks, your account has to be linked to a Google account from the Profile page.

The tool itself is free. The cost to plan for is model usage from your Claude Code, Codex, or Cursor provider, and the built-in cost tracking helps you keep an eye on that in one place.

## Who It Suits

It pays off most for developers who already delegate to more than one agent, small teams that want agent work inside an auditable process, and project leads who need a status overview without checking each terminal. If you only run a single agent now and then, a full board may feel like overkill, though the habit of reviewing output before accepting it is worth building early.

## Other Tools from maserta

maserta is also preparing two other free products. **User Online: Multi-App User Monitoring** is a self-hosted dashboard and server that shows who is online across several applications through WebSocket connections, lets you send messages or maintenance notices, and reports server CPU, RAM, and disk usage. **YouTube HD Downloader** is a Windows desktop app for downloading videos, playlists, and audio with quality and subtitle options, relying on FFmpeg for merging and conversion. Both product pages say they are still being prepared for release, so check maserta.my.id for their current status.

## Bottom Line

MCP Task Manager does not replace your AI agents. It wraps structure around them: written tasks, per-agent tokens, visible progress, and a human review before anything counts as finished. To try it, open task.maserta.my.id, create your first workspace, and connect the agent you already use every day.
