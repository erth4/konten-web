---
title: "APIs Explained: What They Are, How REST Works, and Everyday Examples"
meta_description: "An API lets one application talk to another through requests and responses. Understand REST, HTTP methods, status codes, authentication, and practical examples."
slug: "api-pengertian-cara-kerja-rest-contoh"
focus_keyword: "API"
category: "Technology"
date: "2026-10-10"
lang: "en"
---

# APIs Explained: What They Are, How REST Works, and Everyday Examples

When the weather app on your phone shows the current temperature, it did not measure anything itself. It asked another service for the data. When an online shop offers payment through a digital wallet, the shop is talking to a payment system somewhere else. In both cases, the connector is called an API.

## What Is an API

API stands for Application Programming Interface. Put simply, an API is a set of rules that lets one program request data or services from another without knowing how that program works inside. A common analogy is a restaurant waiter: you give your order to the waiter, the kitchen prepares it, and the waiter brings the result back. You never walk into the kitchen.

## The Basic Flow

The usual pattern is request and response. A client application sends a request to a specific address, called an endpoint. The server processes it and sends back a response, typically in JSON, a format that is easy for both machines and people to read.

For example, a request to one endpoint might ask for a list of articles, and the response contains each article's title, date, and author as structured data.

## What Is REST

REST is a design style for APIs that uses the HTTP protocol. Resources, such as articles or users, are represented by addresses, and the action taken on them is set by the HTTP method:

- **GET** to read data.
- **POST** to create new data.
- **PUT** or **PATCH** to update data.
- **DELETE** to remove data.

REST APIs are generally stateless, meaning each request carries enough information to be processed without the server remembering earlier requests.

## HTTP Status Codes

Every response includes a status code that explains the outcome:

- **200** success.
- **201** new data was created.
- **400** the request was malformed or incomplete.
- **401** not authenticated.
- **403** authenticated but not permitted.
- **404** resource not found.
- **422** data failed validation.
- **429** too many requests.
- **500** an error on the server side.

Reading status codes correctly makes troubleshooting much faster.

## Authentication and Security

Not every API is open to everyone. Common ways to limit access include:

- **API keys**, simple tokens sent along with the request.
- **Bearer tokens**, often issued after login.
- **OAuth**, which gives third-party apps limited access without sharing a password.
- **Sessions and cookies** with a CSRF token, common in web apps that use an admin account.

A few important practices: always use HTTPS, never put secret keys in publicly visible code, grant the least access needed, and rate-limit requests so the API is not abused.

## Everyday Examples

- **Online payments** linking a shop with a payment provider.
- **Maps and location** embedded in delivery apps.
- **Sign in with another account**, which relies on an identity provider's API.
- **Automated content management**, such as adding articles to a website with a script.
- **Internal integrations** between services inside one company.

## APIs and Webhooks

With a regular API, the client asks. With a webhook, the direction flips: the server sends a notification to your address when something happens, such as a successful payment. Webhooks save you from repeatedly asking for status.

## Tips for Designing and Using APIs Well

1. Read the documentation until you understand the request format, response format, and usage limits.
2. Test with a tool like curl or an API client before writing code.
3. Handle errors explicitly, including timeouts and 4xx and 5xx codes.
4. Do not trust incoming data. Validate it on the server.
5. Put a version in the API address, such as `/v1/`, so changes do not break older clients.
6. Log failed requests to make troubleshooting easier.

## Conclusion

An API is essentially an agreement about how two programs talk to each other. Once you understand the flow of requests, methods, and status codes, almost any API you meet will feel familiar. Try calling one public API with curl, look at the response, then change a parameter to see how the behavior changes.
