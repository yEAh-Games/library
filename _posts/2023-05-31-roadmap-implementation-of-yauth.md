---
layout: post
title: "Roadmap: Implementation of yAuth"
author: tallinn
categories: [News, Article, Development]
image: https://news.yeahgames.net/archive/img/yauth.jpg
tags: [sticky, network, dev, timeline, yauth]
link: https://news.yeahgames.net/news/roadmap-implementation-of-yauth
canonical_url: https://news.yeahgames.net/news/roadmap-implementation-of-yauth
c: News
---

As part of our commitment to enhancing user experience and streamlining access to the yEAh Network, we are excited to introduce yAuth, a revolutionary JavaScript-based login system. By leveraging the power of JavaScript and the capabilities of the GitHub & yEAh API, yAuth will provide seamless login functionality, centralized account management, personalized control over user settings, and the ability to stay logged in across our network.

# A JavaScript-Based Login System: Roadmap

## 1\. Planning and Preparation (1-2 weeks)

During this phase, we will meticulously plan and prepare for the implementation of yAuth. We will define technical specifications, outlining the integration of the GitHub/yEAh API as a secure database for storing user information. Detailed consideration will be given to the utilization of JavaScript to query the API and handle authentication processes.

## 2\. Backend Development (3-4 weeks)

In this crucial phase, our backend development team will build a secure infrastructure using the GitHub/yEAh API. User data, such as usernames and encrypted passwords, will be stored within secure GitHub servers. The backend will incorporate client-side APIs to handle user registration, login, and authentication. Passwords will be encrypted using the SHA-256 algorithm for maximum security. No one – not even us – will ever know your password, except you.

## 3\. Frontend Development (4-6 weeks)

The frontend development phase will focus on creating an intuitive and user-friendly login experience. A centralized login page, accounts.yeahgames.net, will be designed using JavaScript. When users enter their credentials, JavaScript functions will query the GitHub/yEAh API to validate the username and match the SHA-256 hashed password with the stored value. Upon successful authentication, a cookie will be written, storing user information such as the username and authentication status.

## 4\. Network Settings and Dynamic Content (3-4 weeks)

In this phase, we will extend the functionality of yAuth to leverage the stored cookie across the yEAh Network. JavaScript functions on other network websites will be developed to query the authentication cookie. This will allow us to display personalized content based on the user's authentication status and permissions. For example, if a user is logged in and has specific permissions, we can display restricted content, such as an iFrame of exclusive games. If a user is not logged in or lacks the necessary permissions, they will be automatically redirected to accounts.yeahgames.net to log in and obtain the authentication cookie.

## 5\. Stay Logged In Functionality (1-2 weeks)

To ensure a seamless and convenient experience, we will implement a "stay logged in" feature using the authentication cookie. When a user logs in, an option will be provided to remain logged in across multiple sessions. JavaScript functions will be developed to check for the presence of the authentication cookie upon subsequent visits to any network website. If the cookie exists and is valid, the user will be automatically authenticated, eliminating the need for repeated logins.

## 6\. Database Management (2-3 weeks)

We will implement a database management system using the GitHub/yEAh API. User data, including account settings and network-specific preferences, will be written directly to the GitHub file. JavaScript functions will read from the GitHub Pages version of the database, ensuring that the most up-to-date information is available for querying and displaying on network websites.

## 7\. Retirement of Existing Login/Token Method (1-2 weeks)

In tandem with the implementation of yAuth, we will retire our existing login/token method, notably used with the quotes library collection Previously, to access any page within this collection, users were redirected to login.yeahgames.net/token/TOKEN and required to enter and decrypt a standard password. This method lacked security and only redirected users to a different subdomain with the content, without dynamically loading it. yAuth will replace this outdated method, providing a more secure and seamless login experience.

Throughout the implementation process, our progress can be tracked on [projects.yeahgames.net](https://projects.yeahgames.net), specifically in the "yAuth" project. Developers can find detailed information, including open-source contributions, on [dev.yeahgames.net/projects/open/yauth](dev.yeahgames.net/projects/open/yauth). Additionally, comprehensive documentation is available at [docs.yeahgames.net](https://docs.yeahgames.net), providing guidance on yAuth implementation, usage, and customization.

## 8. Full project open-sourcing (6+ weeks)

We are committed to fostering innovation and embracing emerging technologies in our quest to provide the best user experience possible. As part of our vision, we plan to gradually open-source the yAuth project. This move aims to offer an innovative alternative to traditional server-side logins, particularly suited for static sites where direct access to the webserver may not be available.

By open-sourcing yAuth, we aim to empower developers in the jamstack community, who heavily rely on JavaScript and dynamic websites. The flexibility and simplicity of yAuth make it a valuable addition to the toolbox of developers seeking to build secure and efficient login systems without the need for complex server-side setups.

We believe in the power of collaboration and the collective wisdom of the developer community. By open-sourcing yAuth, we invite developers from around the world to contribute their expertise, suggest improvements, and shape the future of decentralized login systems. Together, we can build a more inclusive and vibrant ecosystem for web development.

As we progress with the implementation and refinement of yAuth, we will provide updates on the open-source aspect of the project. Stay tuned for announcements regarding the availability of the source code and opportunities for community involvement.

We are excited about the potential of yAuth and its ability to revolutionize login systems for static and jamstack-based websites. We invite developers to join us on this journey and help shape the future of decentralized authentication through our development community at [dev.yeahgames.net](https://dev.yeahgames.net) or by directly contributing to our GitHub repository, [github.com/yeah-games/yauth](https://github.com/yeah-games/yauth).

<hr>

# Contact us

We are excited about the possibilities that yAuth brings to our network community. By providing a robust and user-centric login system, we aim to enhance the overall user experience and enable users to effortlessly navigate and control their settings across the yEAh Network.

For media inquiries, please contact our press representative, [Torin](https://members.yeahgames.net/@nnillat), at [torin@yeahgames.net](mailto:torin@yeahgames.net). Any questions, concerns, or feedback can be forwarded to our development team at [dev@yeahgames.net](mailto:dev@yeahgames.net) or our administrative team at [admin@yeahgames.net](mailto:admin@yeahgames.net).

We are dedicated to ensuring a smooth transition and are here to address any questions or concerns you may have. Stay tuned for updates as we embark on this exciting journey towards a more streamlined and user-friendly network login system.
