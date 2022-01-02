# Greenipy

🌱 Green-ify your GitHub stats using `bash` and `python`.

## Setup

- Create a template repository by [clicking here](https://github.com/laymoth/greenipy/generate)
- Create repository secret (Repo settings > Secrets > Actions > New Repository Secret)
- Fill the name with `COMMIT_EMAIL` and fill the value with your git commit email
> **Note**
> If you don't want use repository secret, just remove `${{ secrets.COMMIT_EMAIL }}` and fill it with your commit email

- Change the commit user name with your name
- Uncomment line 6 & 7
- Adjust the schedule as you like. Pls visit [crontab.guru](https://crontab.guru/)


## Credits

- [Github Actions](https://github.com/features/actions)
- [ad-m/github-push-action](https://github.com/ad-m/github-push-action)