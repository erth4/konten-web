---
title: "Passkeys: Passwordless Login, How They Work, and How to Turn Them On"
meta_description: "Passkeys replace passwords with cryptographic keys stored on your device. Learn how they work, where they help, where they fall short, and how to start using them."
slug: "passkey-login-tanpa-kata-sandi-cara-kerja"
focus_keyword: "passkey"
category: "Technology"
date: "2026-10-10"
lang: "en"
---

# Passkeys: Passwordless Login, How They Work, and How to Turn Them On

Passwords have long been the weakest point in account security. People reuse the same one across services, choose combinations that are easy to guess, or get fooled by a fake login page. Passkeys take a different route: there is nothing to remember, type, or steal.

## What Is a Passkey

A passkey is a login credential that replaces a password. Instead of a string of characters, your account is tied to a pair of cryptographic keys. One is public and stored on the service's server. The other is private and stays on your device. To sign in, you unlock that private key with a fingerprint, face scan, or device PIN.

Passkeys are built on the open WebAuthn and FIDO2 standards, developed through industry cooperation. Because they are standards, they work across browsers and operating systems that support them.

## How Passkeys Work

The process has two stages.

**Registration.** When you create a passkey for a website, your device generates a new key pair. The public key is sent to the site and stored with your account. The private key never leaves your device or your secure credential store.

**Sign-in.** When you log in, the site sends a challenge made of random data. Your device signs it with the private key after you verify yourself locally. The site checks the signature against the public key. If it matches, you are in.

Fingerprint or face verification happens on your device. Biometric data is not sent to the site.

## Why They Are Safer

- **Phishing resistant.** A passkey is bound to the real domain of the site. A fake page at a different address cannot request a valid signature.
- **No shared secret on the server.** The server holds only a public key. If its database leaks, attackers get nothing they can use to log in.
- **Unique for every service.** A passkey cannot be reused, so a breach in one place does not spread to others.
- **Nothing to memorize or type**, which makes password guessing and credential stuffing irrelevant.

## Where Passkeys Are Stored

There are two common approaches. Synced passkeys live in an account-based service, such as a password manager or your operating system's credential store, and copy to other devices on the same account. This is convenient, because replacing your phone does not lock you out. Device-bound passkeys, for example on a physical security key, exist on a single piece of hardware. They are more tightly controlled but harder to recover if the device is lost.

## Limits to Know About

Passkeys are not flawless. First, not every site and app supports them yet, so passwords will sit alongside them for a while. Second, the security of a synced passkey depends on the security of the account that stores it, so that account needs two-step verification and a clear recovery path. Third, moving between ecosystems can be awkward, depending on what each service supports. Finally, if your device is stolen and its PIN is known, an attacker could try to unlock those credentials.

## How to Start Using Passkeys

1. **Get your device ready.** Turn on the screen lock, biometrics, and the latest system updates.
2. **Check service support.** Open your account's security settings and look for "passkey" or "passwordless sign-in".
3. **Create the passkey.** Follow the prompts and verify with a fingerprint, face, or PIN.
4. **Choose where it is stored.** Use a credential manager you trust and protect it with two-step verification.
5. **Set up recovery.** Keep a backup method somewhere safe before removing your old password.
6. **Start with important accounts.** Email, banking, and any account that unlocks other services deserve priority.

## Conclusion

Passkeys do not remove every risk, but they close the two doors attackers use most often: weak passwords and fake login pages. Try turning one on for a single important account this week while keeping a recovery route in place. Once it feels natural, extend it to other services as more of them add support.
