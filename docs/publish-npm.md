# Publish To npm

Use this guide when releasing `@thanhndpo/tanizy-po-agent` or a generated target-specific package.

## Release Checklist

1. Update the package version in `package.json`. An npm package version cannot be reused after it has been published.
2. Review the package contents:

   ```bash
   npm run pack:check
   ```

3. Build and validate target-specific packages when they are part of the release:

   ```bash
   npm run build:target-packages
   for package_dir in dist/packages/*; do
     node scripts/check-published-package.mjs "$package_dir"
   done
   ```

4. Check the npm account:

   ```bash
   npm whoami
   ```

5. Publish the universal package interactively:

   ```bash
   npm publish --access public
   ```

## 2FA and npm Authentication

Do not hard-code `--otp` into the standard publish command. Depending on the npm account, CLI version, authentication method, and current npm policy, npm may complete authentication through a browser or another interactive flow without requiring the OTP as a command-line argument.

If npm explicitly asks for a one-time password, follow the prompt or use:

```bash
npm publish --access public --otp <one-time-password>
```

Never commit an OTP, access token, or `.npmrc` containing credentials.

According to the [npm security policy changelog](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/):

- npm v12 enables install-time security defaults. Lifecycle scripts, Git dependencies, and remote URL dependencies that were previously automatic now require explicit opt-in in the relevant situations.
- 2FA-bypass granular access tokens are being deprecated for sensitive account, package, and organization management actions.
- 2FA-bypass tokens are planned to lose direct publishing ability around January 2027. Automated publishing should move to [Trusted Publishing with OIDC](https://docs.npmjs.com/trusted-publishers) or [Staged Publishing](https://docs.npmjs.com/cli/v11/commands/npm-publish#staged-publishing) with a human approval step.

## Publish A Target-Specific Package

Generate the packages first:

```bash
npm run build:target-packages
```

Review one package, then publish it from its generated directory:

```bash
node scripts/check-published-package.mjs dist/packages/codex
npm publish dist/packages/codex --access public
```

Repeat for the other target only when the package is ready for release.

## Verify The Release

After publishing, verify the registry version:

```bash
npm view @thanhndpo/tanizy-po-agent version
npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --dry-run
```

For the `0.1.2` release, the universal package contains the integrated `generating-mockup` and `shadcn-ui` skills.
