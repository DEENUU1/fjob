import DOMPurify from "dompurify";

const myHTML = `<style>
    [data-custom-class='body'], [data-custom-class='body'] * {
        background: transparent !important;
    }

    [data-custom-class='title'], [data-custom-class='title'] * {
        font-family: Arial !important;
        font-size: 26px !important;
        color: #000000 !important;
    }

    [data-custom-class='subtitle'], [data-custom-class='subtitle'] * {
        font-family: Arial !important;
        color: #595959 !important;
        font-size: 14px !important;
    }

    [data-custom-class='heading_1'], [data-custom-class='heading_1'] * {
        font-family: Arial !important;
        font-size: 19px !important;
        color: #000000 !important;
    }

    [data-custom-class='heading_2'], [data-custom-class='heading_2'] * {
        font-family: Arial !important;
        font-size: 17px !important;
        color: #000000 !important;
    }

    [data-custom-class='body_text'], [data-custom-class='body_text'] * {
        color: #595959 !important;
        font-size: 14px !important;
        font-family: Arial !important;
    }

    [data-custom-class='link'], [data-custom-class='link'] * {
        color: #3030F1 !important;
        font-size: 14px !important;
        font-family: Arial !important;
        word-break: break-word !important;
    }
</style>

<div data-custom-class="body">
    <div><strong><span style="font-size: 26px;"><span data-custom-class="title"><bdt class="block-component"></bdt><bdt
            class="question">PRIVACY POLICY</bdt><bdt class="statement-end-if-in-editor"></bdt></span></span></strong>
    </div>
    <div><br></div>
    <div><span style="color: rgb(127, 127, 127);"><strong><span style="font-size: 15px;"><span
            data-custom-class="subtitle">Last updated <bdt
            class="question">November 06, 2023</bdt></span></span></strong></span></div>
    <div><br></div>
    <div><br></div>
    <div><br></div>
    <div style="line-height: 1.5;"><span style="color: rgb(127, 127, 127);"><span
            style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text">This privacy notice for <bdt
            class="question">FJob<bdt class="block-component"></bdt></bdt> (<bdt class="block-component"></bdt>'<strong>we</strong>', '<strong>us</strong>', or '<strong>our</strong>'<bdt
            class="else-block"></bdt></span><span data-custom-class="body_text">), describes how and why we might collect, store, use, and/or share (<bdt
            class="block-component"></bdt>'<strong>process</strong>'<bdt class="else-block"></bdt>) your information when you use our services (<bdt
            class="block-component"></bdt>'<strong>Services</strong>'<bdt class="else-block"></bdt>), such as when you:</span></span></span><span
            style="font-size: 15px;"><span style="color: rgb(127, 127, 127);"><span data-custom-class="body_text"><span
            style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
            class="block-component"></bdt></span></span></span></span></span></div>
    <ul>
        <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">Visit our website<bdt
                class="block-component"></bdt> at <span style="color: rgb(0, 58, 250);"><bdt
                class="question">fjob.com</bdt></span><span style="font-size: 15px;"><span
                style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span style="font-size: 15px;"><span
                style="color: rgb(89, 89, 89);"><bdt class="statement-end-if-in-editor">, or any website of ours that links to this privacy notice</bdt></span></span></span></span></span></span></span></span>
        </li>
    </ul>
    <div>
        <bdt class="block-component"><span style="font-size: 15px;"><span style="font-size: 15px;"><span
                style="color: rgb(127, 127, 127);"><span data-custom-class="body_text"><span
                style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt class="block-component"></bdt>
        </bdt>
        </span></span></span></span></span></span></span></span></li></ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span style="color: rgb(127, 127, 127);"><span
                data-custom-class="body_text"><span style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                class="block-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">Engage with us in other related ways, including any sales, marketing, or events<span
                    style="font-size: 15px;"><span style="color: rgb(89, 89, 89);"><span
                    data-custom-class="body_text"><span style="font-size: 15px;"><span style="color: rgb(89, 89, 89);"><bdt
                    class="statement-end-if-in-editor"></bdt></span></span></span></span></span></span></span></span>
            </li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span style="color: rgb(127, 127, 127);"><span
                data-custom-class="body_text"><strong>Questions or concerns? </strong>Reading this privacy notice will help you understand your privacy rights and choices. If you do not agree with our policies and practices, please do not use our Services.<bdt
                class="block-component"></bdt> If you still have any questions or concerns, please contact us at <bdt
                class="question">kacperwlodarczyk@protonmail.com</bdt>.</span></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><strong><span style="font-size: 15px;"><span data-custom-class="heading_1">SUMMARY OF KEY POINTS</span></span></strong>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong><em>This summary provides key points from our privacy notice, but you can find out more details about any of these topics by clicking the link following each key point or by using our </em></strong></span></span><a
                data-custom-class="link" href="#toc"><span style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text"><strong><em>table of contents</em></strong></span></span></a><span
                style="font-size: 15px;"><span data-custom-class="body_text"><strong><em> below to find the section you are looking for.</em></strong></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>What personal information do we process?</strong> When you visit, use, or navigate our Services, we may process personal information depending on how you interact with us and the Services, the choices you make, and the products and features you use. Learn more about </span></span><a
                data-custom-class="link" href="#personalinfo"><span
                style="color: rgb(0, 58, 250); font-size: 15px;"><span data-custom-class="body_text">personal information you disclose to us</span></span></a><span
                data-custom-class="body_text">.</span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>Do we process any sensitive personal information?</strong> <bdt
                class="block-component"></bdt>We do not process sensitive personal information.<bdt
                class="else-block"></bdt></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>Do we receive any information from third parties?</strong> <bdt
                class="block-component"></bdt>We do not receive any information from third parties.<bdt
                class="else-block"></bdt></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>How do we process your information?</strong> We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We may also process your information for other purposes with your consent. We process your information only when we have a valid legal reason to do so. Learn more about </span></span><a
                data-custom-class="link" href="#infouse"><span style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text">how we process your information</span></span></a><span
                data-custom-class="body_text">.</span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>In what situations and with which <bdt
                class="block-component"></bdt>types of <bdt class="statement-end-if-in-editor"></bdt>parties do we share personal information?</strong> We may share information in specific situations and with specific <bdt
                class="block-component"></bdt>categories of <bdt class="statement-end-if-in-editor"></bdt>third parties. Learn more about </span></span><a
                data-custom-class="link" href="#whoshare"><span style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text">when and with whom we share your personal information</span></span></a><span
                style="font-size: 15px;"><span data-custom-class="body_text">.<bdt class="block-component"></bdt></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>How do we keep your information safe?</strong> We have <bdt
                class="block-component"></bdt>organisational<bdt class="else-block"></bdt> and technical processes and procedures in place to protect your personal information. However, no electronic transmission over the internet or information storage technology can be guaranteed to be 100% secure, so we cannot promise or guarantee that hackers, cybercriminals, or other <bdt
                class="block-component"></bdt>unauthorised<bdt class="else-block"></bdt> third parties will not be able to defeat our security and improperly collect, access, steal, or modify your information. Learn more about </span></span><a
                data-custom-class="link" href="#infosafe"><span style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text">how we keep your information safe</span></span></a><span
                data-custom-class="body_text">.</span><span style="font-size: 15px;"><span
                data-custom-class="body_text"><bdt class="statement-end-if-in-editor"></bdt></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>What are your rights?</strong> Depending on where you are located geographically, the applicable privacy law may mean you have certain rights regarding your personal information. Learn more about </span></span><a
                data-custom-class="link" href="#privacyrights"><span
                style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text">your privacy rights</span></span></a><span
                data-custom-class="body_text">.</span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><strong>How do you exercise your rights?</strong> The easiest way to exercise your rights is by <bdt
                class="block-component">submitting a </bdt></span></span><a data-custom-class="link"
                                                                            href="https://app.termly.io/notify/e4effab4-134f-44f5-ab80-0c1566c85de2"
                                                                            rel="noopener noreferrer"
                                                                            target="_blank"><span
                style="color: rgb(0, 58, 250); font-size: 15px;"><span data-custom-class="body_text">data subject access request</span></span></a><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt class="block-component"></bdt>, or by contacting us. We will consider and act upon any request in accordance with applicable data protection laws.</span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text">Want to learn more about what we do with any information we collect? </span></span><a
                data-custom-class="link" href="#toc"><span style="color: rgb(0, 58, 250); font-size: 15px;"><span
                data-custom-class="body_text">Review the privacy notice in full</span></span></a><span
                style="font-size: 15px;"><span data-custom-class="body_text">.</span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><br></div>
        <div id="toc" style="line-height: 1.5;"><span style="font-size: 15px;"><span style="color: rgb(127, 127, 127);"><span
                style="color: rgb(0, 0, 0);"><strong><span
                data-custom-class="heading_1">TABLE OF CONTENTS</span></strong></span></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link"
                                                                         href="#infocollect"><span
                style="color: rgb(0, 58, 250);">1. WHAT INFORMATION DO WE COLLECT?</span></a></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link" href="#infouse"><span
                style="color: rgb(0, 58, 250);">2. HOW DO WE PROCESS YOUR INFORMATION?<bdt
                class="block-component"></bdt></span></a></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link"
                                                                         href="#legalbases"><span
                style="color: rgb(0, 58, 250);">3. <span style="font-size: 15px;"><span style="color: rgb(0, 58, 250);">WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR PERSONAL INFORMATION?</span></span><bdt
                class="statement-end-if-in-editor"></bdt></span></a></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span style="color: rgb(0, 58, 250);"><a
                data-custom-class="link"
                href="#whoshare">4. WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?</a></span><span
                data-custom-class="body_text"><bdt class="block-component"></bdt></span></span></div>
        <div style="line-height: 1.5;"><span style="color: rgb(0, 58, 250); font-size: 15px;"><a
                data-custom-class="link" href="#3pwebsites">5. WHAT IS OUR STANCE ON THIRD-PARTY WEBSITES?<bdt
                class="statement-end-if-in-editor"></bdt></a><span style="color: rgb(127, 127, 127);"><span
                style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="color: rgb(89, 89, 89);"><bdt class="block-component"></bdt></span></span></span></span></span>
        </div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link" href="#cookies"><span
                style="color: rgb(0, 58, 250);">6. DO WE USE COOKIES AND OTHER TRACKING TECHNOLOGIES?</span></a><span
                style="color: rgb(127, 127, 127);"><span style="color: rgb(89, 89, 89);"><span
                data-custom-class="body_text"><span style="color: rgb(89, 89, 89);"><bdt
                class="statement-end-if-in-editor"></bdt></span></span><span data-custom-class="body_text"><span
                style="color: rgb(89, 89, 89);"><span style="color: rgb(89, 89, 89);"><span
                style="color: rgb(89, 89, 89);"><bdt class="block-component"></bdt></span></span><bdt
                class="block-component"></bdt></span></span></span></span></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link"
                                                                         href="#inforetain"><span
                style="color: rgb(0, 58, 250);">7. HOW LONG DO WE KEEP YOUR INFORMATION?</span></a><span
                style="color: rgb(127, 127, 127);"><span style="color: rgb(89, 89, 89);"><span
                data-custom-class="body_text"><span style="color: rgb(89, 89, 89);"><span
                style="color: rgb(89, 89, 89);"><bdt
                class="block-component"></bdt></span></span></span></span></span></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link" href="#infosafe"><span
                style="color: rgb(0, 58, 250);">8. HOW DO WE KEEP YOUR INFORMATION SAFE?</span></a><span
                style="color: rgb(127, 127, 127);"><span style="color: rgb(89, 89, 89);"><span
                data-custom-class="body_text"><span style="color: rgb(89, 89, 89);"><bdt
                class="statement-end-if-in-editor"></bdt><bdt class="block-component"></bdt></span></span></span></span></span>
        </div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span style="color: rgb(0, 58, 250);"><a
                data-custom-class="link" href="#privacyrights">9. WHAT ARE YOUR PRIVACY RIGHTS?</a></span></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link" href="#DNT"><span
                style="color: rgb(0, 58, 250);">10. CONTROLS FOR DO-NOT-TRACK FEATURES<bdt
                class="block-component"></span><bdt class="block-component"><span style="font-size: 15px;"><span
                data-custom-class="body_text"></span></bdt></span></div>
        <div style="line-height: 1.5;">
            <bdt class="block-component"><span style="font-size: 15px;"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></bdt>
            <bdt class="block-component"></span></bdt>
        </div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><a data-custom-class="link" href="#policyupdates"><span
                style="color: rgb(0, 58, 250);">11. DO WE MAKE UPDATES TO THIS NOTICE?</span></a></span></div>
        <div style="line-height: 1.5;"><a data-custom-class="link" href="#contact"><span
                style="color: rgb(0, 58, 250); font-size: 15px;">12. HOW CAN YOU CONTACT US ABOUT THIS NOTICE?</span></a>
        </div>
        <div style="line-height: 1.5;"><a data-custom-class="link" href="#request"><span
                style="color: rgb(0, 58, 250);">13. HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?</span></a>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><br></div>
        <div id="infocollect" style="line-height: 1.5;"><span style="color: rgb(0, 0, 0);"><span
                style="color: rgb(0, 0, 0); font-size: 15px;"><span style="font-size: 15px; color: rgb(0, 0, 0);"><span
                style="font-size: 15px; color: rgb(0, 0, 0);"><span id="control"
                                                                    style="color: rgb(0, 0, 0);"><strong><span
                data-custom-class="heading_1">1. WHAT INFORMATION DO WE COLLECT?</span></strong></span></span></span></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div id="personalinfo" style="line-height: 1.5;"><span data-custom-class="heading_2"
                                                               style="color: rgb(0, 0, 0);"><span
                style="font-size: 15px;"><strong>Personal information you disclose to us</strong></span></span></div>
        <div>
            <div><br></div>
            <div style="line-height: 1.5;"><span style="color: rgb(127, 127, 127);"><span
                    style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong><em>In Short:</em></strong></span></span></span></span><span
                    data-custom-class="body_text"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    data-custom-class="body_text"><strong><em> </em></strong><em>We collect personal information that you provide to us.</em></span></span></span></span></span></span>
            </div>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">We collect personal information that you voluntarily provide to us when you <span
                style="font-size: 15px;"><bdt
                class="block-component"></bdt></span>register on the Services, </span><span
                style="font-size: 15px;"><span data-custom-class="body_text"><span style="font-size: 15px;"><bdt
                class="statement-end-if-in-editor"></bdt></span></span><span data-custom-class="body_text">express an interest in obtaining information about us or our products and Services, when you participate in activities on the Services, or otherwise when you contact us.</span></span></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><bdt class="block-component"></bdt></span></span></span></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong>Personal Information Provided by You.</strong> The personal information that we collect depends on the context of your interactions with us and the Services, the choices you make, and the products and features you use. The personal information we collect may include the following:<span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="question">phone numbers</bdt></span></span></span></span></span></li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="question">email addresses</bdt></span></span></span></span></span></li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="question">mailing addresses</bdt></span></span></span></span></span></li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="question">usernames</bdt></span></span></span></span></span></li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span></span></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="question">passwords</bdt></span></span></span></span></span></li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="forloop-component"></bdt></span><span data-custom-class="body_text"><bdt
                class="statement-end-if-in-editor"></bdt></span></span></span></span></span></div>
        <div id="sensitiveinfo" style="line-height: 1.5;"><span style="font-size: 15px;"><span
                data-custom-class="body_text"><strong>Sensitive Information.</strong> <bdt
                class="block-component"></bdt>We do not process sensitive information.</span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="else-block"></bdt></span></span><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                style="font-size: 15px;"><span data-custom-class="body_text"><bdt class="block-component"><bdt
                class="block-component"></bdt></bdt></span></span></span></span><bdt
                class="block-component"></span></span></bdt></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">All personal information that you provide to us must be true, complete, and accurate, and you must notify us of any changes to such personal information.</span></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                class="block-component"></bdt></span></span></span></div>
        <div style="line-height: 1.5;"><span data-custom-class="heading_2" style="color: rgb(0, 0, 0);"><span
                style="font-size: 15px;"><strong>Information automatically collected</strong></span></span></div>
        <div>
            <div><br></div>
            <div style="line-height: 1.5;"><span style="color: rgb(127, 127, 127);"><span
                    style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong><em>In Short:</em></strong></span></span></span></span><span
                    data-custom-class="body_text"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    data-custom-class="body_text"><strong><em> </em></strong><em>Some information — such as your Internet Protocol (IP) address and/or browser and device characteristics — is collected automatically when you visit our Services.</em></span></span></span></span></span></span>
            </div>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">We automatically collect certain information when you visit, use, or navigate the Services. This information does not reveal your specific identity (like your name or contact information) but may include device and usage information, such as your IP address, browser and device characteristics, operating system, language preferences, referring URLs, device name, country, location, information about how and when you use our Services, and other technical information. This information is primarily needed to maintain the security and operation of our Services, and for our internal analytics and reporting purposes.</span></span></span>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                class="block-component"></bdt></span></span></span></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text">Like many businesses, we also collect information through cookies and similar technologies. <bdt
                class="block-component"></bdt><bdt class="block-component"></bdt></span></span></span></div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                class="statement-end-if-in-editor"><span data-custom-class="body_text"></span></bdt></span><span
                data-custom-class="body_text"><bdt class="block-component"></bdt><bdt
                class="statement-end-if-in-editor"></bdt>
            </bdt></span><span data-custom-class="body_text"><span
                style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text"><span
                style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text"><bdt
                class="statement-end-if-in-editor"><bdt
                class="block-component"></bdt></bdt></span></span></span></span></bdt></span></span></span></span></span></span></span></span>
            <span style="font-size: 15px;"><span data-custom-class="body_text"><bdt
                    class="block-component"></bdt></span></span></div>
        <div id="infouse" style="line-height: 1.5;"><span style="color: rgb(127, 127, 127);"><span
                style="color: rgb(89, 89, 89); font-size: 15px;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span id="control"
                                                                       style="color: rgb(0, 0, 0);"><strong><span
                data-custom-class="heading_1">2. HOW DO WE PROCESS YOUR INFORMATION?</span></strong></span></span></span></span></span>
        </div>
        <div>
            <div style="line-height: 1.5;"><br></div>
            <div style="line-height: 1.5;"><span style="color: rgb(127, 127, 127);"><span
                    style="color: rgb(89, 89, 89); font-size: 15px;"><span data-custom-class="body_text"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong><em>In Short: </em></strong><em>We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We may also process your information for other purposes with your consent.</em></span></span></span></span></span></span>
            </div>
        </div>
        <div style="line-height: 1.5;"><br></div>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong>We process your personal information for a variety of reasons, depending on how you interact with our Services, including:</strong><bdt
                class="block-component"></bdt></span></span></span></div>
        <ul>
            <li style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><strong>To facilitate account creation and authentication and otherwise manage user accounts. </strong>We may process your information so you can create and log in to your account, as well as keep your account in working order.<span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><span
                    style="font-size: 15px;"><span style="color: rgb(89, 89, 89);"><span
                    data-custom-class="body_text"><span style="font-size: 15px;"><span
                    style="color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                    class="statement-end-if-in-editor"></bdt></span></span></span></span></span></span></span></span></span></span></span></span>
            </li>
        </ul>
        <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                class="block-component"></bdt></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li></ul>
            <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                    style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                    class="block-component"></bdt></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li></ul>
                <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                        style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                        class="block-component"></bdt></span></span></span></span></span></span></span></span></span></span></span></span></li></ul>
                    <div style="line-height: 1.5;"><span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                            style="font-size: 15px; color: rgb(89, 89, 89);"><span data-custom-class="body_text"><bdt
                            class="block-component"></bdt></span></span></span></li></ul>
                        <div style="line-height: 1.5;">
                            <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                            </span></span></span></span></span></span></li></ul>
                            <div style="line-height: 1.5;">
                                <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                </span></span></span></span></span></span></span></span></span></li></ul>
                                <div style="line-height: 1.5;">
                                    <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                    </span></span></span></span></span></span></span></span></span></span></span></span></li></ul>
                                    <div style="line-height: 1.5;">
                                        <bdt class="block-component"><span style="font-size: 15px;"><span
                                                data-custom-class="body_text"></span></span></bdt>
                                        </li></ul>
                                        <p style="font-size: 15px; line-height: 1.5;">
                                            <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                            </span></span></span></span></span></span></span></span></span></span></span></li></ul>
                                        <p style="font-size: 15px; line-height: 1.5;">
                                            <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                            </span></span></span></span></span></span></span></span></span></span></span></li></ul>
                                        <p style="font-size: 15px; line-height: 1.5;">
                                            <bdt class="block-component"></bdt>
                                            </span></span></span></span></span></span></span></span></span></span></span></li></ul>
                                        <p style="font-size: 15px; line-height: 1.5;">
                                            <bdt class="block-component"></bdt>
                                            </span></span></span></span></span></span></span></span></span></span></span></li></ul>
                                        <div style="line-height: 1.5;">
                                            <bdt class="block-component"><span style="font-size: 15px;"><span
                                                    data-custom-class="body_text"></span></bdt>
                                            </span></li></ul>
                                            <div style="line-height: 1.5;">
                                                <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                                </span></span></span></li></ul>
                                                <div style="line-height: 1.5;">
                                                    <bdt class="block-component"><span style="font-size: 15px;"></bdt>
                                                    </span></span></span></li></ul>
                                                    <div style="line-height: 1.5;"><span style="font-size: 15px;"><bdt
                                                            class="block-component"><span data-custom-class="body_text"></bdt></span></span></li></ul>
                                                        <div style="line-height: 1.5;">
                                                            <bdt class="block-component"><span style="font-size: 15px;"><span
                                                                    data-custom-class="body_text"></bdt>
                                                            </span></span></li></ul>
                                                            <div style="line-height: 1.5;">
                                                                <bdt class="block-component"><span
                                                                        style="font-size: 15px;"><span
                                                                        data-custom-class="body_text"></span></span>
                                                                </bdt>
                                                                </li></ul>
                                                                <div style="line-height: 1.5;">
                                                                    <bdt class="block-component"><span
                                                                            style="font-size: 15px;"><span
                                                                            data-custom-class="body_text"></span></span>
                                                                    </bdt>
                                                                    </li></ul>
                                                                    <div style="line-height: 1.5;">
                                                                        <bdt class="block-component"><span
                                                                                style="font-size: 15px;"><span
                                                                                data-custom-class="body_text"></span></span>
                                                                        </bdt>
                                                                        </li></ul>
                                                                        <div style="line-height: 1.5;">
                                                                            <bdt class="block-component"><span
                                                                                    style="font-size: 15px;"><span
                                                                                    data-custom-class="body_text"></span></span>
                                                                            </bdt>
                                                                            </li></ul>
                                                                            <div style="line-height: 1.5;">
                                                                                <bdt class="block-component"><span
                                                                                        style="font-size: 15px;"><span
                                                                                        data-custom-class="body_text"></span></span>
                                                                                </bdt>
                                                                                </li></ul>
                                                                                <div style="line-height: 1.5;">
                                                                                    <bdt class="block-component"><span
                                                                                            style="font-size: 15px;"><span
                                                                                            data-custom-class="body_text"></span></span>
                                                                                    </bdt>
                                                                                    </li></ul>
                                                                                    <div style="line-height: 1.5;">
                                                                                        <bdt class="block-component">
                                                                                            <span style="font-size: 15px;"><span
                                                                                                    data-custom-class="body_text">
                                                                                        </bdt>
                                                                                        </span></span></li></ul>
                                                                                        <div style="line-height: 1.5;">
                                                                                            <bdt class="block-component">
                                                                                                <span style="font-size: 15px;"><span
                                                                                                        data-custom-class="body_text">
                                                                                            </bdt>
                                                                                            </span></span></li></ul>
                                                                                            <div style="line-height: 1.5;">
                                                                                                <bdt class="block-component">
                                                                                                    <span style="font-size: 15px;"><span
                                                                                                            data-custom-class="body_text">
                                                                                                </bdt>
                                                                                                </span></span></li></ul>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"></span></span>
                                                                                                    </bdt>
                                                                                                </div>
                                                                                                <ul>
                                                                                                    <li style="line-height: 1.5;">
                                                                                                        <span data-custom-class="body_text"><span
                                                                                                                style="font-size: 15px;"><strong>To save or protect an individual's vital interest.</strong> We may process your information when necessary to save or protect an individual’s vital interest, such as to prevent harm.</span></span>
                                                                                                        <bdt class="statement-end-if-in-editor">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                    </li>
                                                                                                </ul>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"></span></span>
                                                                                                    </bdt>
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text">
                                                                                                    </bdt>
                                                                                                    </span></span>
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"></span></span>
                                                                                                    </bdt>
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"></span></span>
                                                                                                    </bdt>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <br></div>
                                                                                                <div id="legalbases"
                                                                                                     style="line-height: 1.5;">
                                                                                                    <strong><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            data-custom-class="heading_1">3. WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR INFORMATION?</span></span></strong>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <br></div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <em><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            data-custom-class="body_text"><strong>In Short: </strong>We only process your personal information when we believe it is necessary and we have a valid legal reason (i.e.<bdt
                                                                                                            class="block-component"></bdt> legal basis) to do so under applicable law, like with your consent, to comply with laws, to provide you with services to enter into or <bdt
                                                                                                            class="block-component"></bdt>fulfil<bdt
                                                                                                            class="else-block"></bdt> our contractual obligations, to protect your rights, or to <bdt
                                                                                                            class="block-component"></bdt>fulfil<bdt
                                                                                                            class="else-block"></bdt> our legitimate business interests.</span></span></em><span
                                                                                                        style="font-size: 15px;"><span
                                                                                                        data-custom-class="body_text"><bdt
                                                                                                        class="block-component"></bdt></span><span
                                                                                                        data-custom-class="body_text"><bdt
                                                                                                        class="block-component"></bdt></span></span>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <br></div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span style="font-size: 15px;"><span
                                                                                                            data-custom-class="body_text">The General Data Protection Regulation (GDPR) and UK GDPR require us to explain the valid legal bases we rely on in order to process your personal information. As such, we may rely on the following legal bases to process your personal information:</span></span>
                                                                                                </div>
                                                                                                <ul>
                                                                                                    <li style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"><strong>Consent. </strong>We may process your information if you have given us permission (i.e.<bdt
                                                                                                                class="block-component"></bdt> consent) to use your personal information for a specific purpose. You can withdraw your consent at any time. Learn more about </span></span><a
                                                                                                            data-custom-class="link"
                                                                                                            href="#withdrawconsent"><span
                                                                                                            style="color: rgb(0, 58, 250); font-size: 15px;"><span
                                                                                                            data-custom-class="body_text">withdrawing your consent</span></span></a><span
                                                                                                            data-custom-class="body_text">.</span>
                                                                                                    </li>
                                                                                                </ul>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <bdt class="block-component">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"></span></span>
                                                                                                    </bdt>
                                                                                                    </li></ul>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <bdt class="block-component">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                        <bdt class="block-component">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span data-custom-class="body_text"><span
                                                                                                                    style="font-size: 15px;"><strong>Legal Obligations.</strong> We may process your information where we believe it is necessary for compliance with our legal obligations, such as to cooperate with a law enforcement body or regulatory agency, exercise or defend our legal rights, or disclose your information as evidence in litigation in which we are involved.<bdt
                                                                                                                    class="statement-end-if-in-editor"></bdt><br></span></span>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <bdt class="block-component">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span data-custom-class="body_text"><span
                                                                                                                    style="font-size: 15px;"><strong>Vital Interests.</strong> We may process your information where we believe it is necessary to protect your vital interests or the vital interests of a third party, such as situations involving potential threats to the safety of any person.</span></span>
                                                                                                            <bdt class="statement-end-if-in-editor">
                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                            </bdt>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <bdt class="block-component">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                        <span data-custom-class="body_text"><span
                                                                                                                style="font-size: 15px;"><bdt
                                                                                                                class="block-component"><bdt
                                                                                                                class="block-component"></span></span></bdt>
                                                                                                        <bdt class="statement-end-if-in-editor">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                        </bdt>
                                                                                                    </div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <br></div>
                                                                                                    <div id="whoshare"
                                                                                                         style="line-height: 1.5;">
                                                                                                        <span style="color: rgb(127, 127, 127);"><span
                                                                                                                style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                id="control"
                                                                                                                style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                data-custom-class="heading_1">4. WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?</span></strong></span></span></span></span></span>
                                                                                                    </div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <br></div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                data-custom-class="body_text"><strong><em>In Short:</em></strong><em> We may share information in specific situations described in this section and/or with the following <bdt
                                                                                                                class="block-component"></bdt>categories of <bdt
                                                                                                                class="statement-end-if-in-editor"></bdt>third parties.</em></span></span></span>
                                                                                                    </div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                data-custom-class="body_text"><bdt
                                                                                                                class="block-component"></bdt></span></span></span>
                                                                                                    </div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <br></div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"><strong>Vendors, Consultants, and Other Third-Party Service Providers.</strong> We may share your data with third-party vendors, service providers, contractors, or agents (<bdt
                                                                                                                class="block-component"></bdt>'<strong>third parties</strong>'<bdt
                                                                                                                class="else-block"></bdt>) who perform services for us or on our behalf and require access to such information to do that work. <bdt
                                                                                                                class="block-component"></bdt>We have contracts in place with our third parties, which are designed to help safeguard your personal information. This means that they cannot do anything with your personal information unless we have instructed them to do it. They will also not share your personal information with any <bdt
                                                                                                                class="block-component"></bdt>organisation<bdt
                                                                                                                class="else-block"></bdt> apart from us. They also commit to protect the data they hold on our behalf and to retain it for the period we instruct. <bdt
                                                                                                                class="statement-end-if-in-editor"></bdt>The <bdt
                                                                                                                class="block-component"></bdt>categories of <bdt
                                                                                                                class="statement-end-if-in-editor"></bdt>third parties we may share personal information with are as follows:</span></span><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><bdt
                                                                                                            class="block-component"></bdt><bdt
                                                                                                            class="forloop-component"></bdt></span>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                    class="question">Ad Networks</bdt></span></span></span>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><bdt
                                                                                                            class="block-component"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><bdt
                                                                                                            class="forloop-component"></bdt></span>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                    class="question">Cloud Computing Services</bdt></span></span></span>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><bdt
                                                                                                            class="block-component"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><bdt
                                                                                                            class="forloop-component"></bdt></span>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                    class="question">Website Hosting Service Providers</bdt></span></span></span>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><bdt
                                                                                                            class="block-component"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><bdt
                                                                                                            class="forloop-component"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            data-custom-class="body_text"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><span
                                                                                                            style="font-size: 15px;"><span
                                                                                                            style="color: rgb(89, 89, 89);"><bdt
                                                                                                            class="statement-end-if-in-editor"></bdt></span></span></span></span></span></span></span></span></span></span></span></span></bdt></span></span></span></bdt></span></span></span></span></span></span><span
                                                                                                            data-custom-class="body_text"><bdt
                                                                                                            class="block-component"></bdt></span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <bdt class="block-component"></bdt>
                                                                                                        </span></span></span></span></span></span></span></span>
                                                                                                        <span data-custom-class="body_text"></span><span
                                                                                                                data-custom-class="body_text"></span><span
                                                                                                                data-custom-class="body_text"></span><span
                                                                                                                data-custom-class="body_text"></span>
                                                                                                    </div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <br></div>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text">We <bdt
                                                                                                                class="block-component"></bdt>also <bdt
                                                                                                                class="statement-end-if-in-editor"></bdt>may need to share your personal information in the following situations:</span></span>
                                                                                                    </div>
                                                                                                    <ul>
                                                                                                        <li style="line-height: 1.5;">
                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                    data-custom-class="body_text"><strong>Business Transfers.</strong> We may share or transfer your information in connection with, or during negotiations of, any merger, sale of company assets, financing, or acquisition of all or a portion of our business to another company.</span></span>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                    <div style="line-height: 1.5;">
                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                data-custom-class="body_text"><bdt
                                                                                                                class="block-component"></bdt></span></span></li></ul>
                                                                                                        <div style="line-height: 1.5;">
                                                                                                            <span style="font-size: 15px;"><bdt
                                                                                                                    class="block-component"><span
                                                                                                                    data-custom-class="body_text"></span></bdt></span></li></ul>
                                                                                                            <div style="line-height: 1.5;">
                                                                                                                <bdt class="block-component">
                                                                                                                    <span style="font-size: 15px;"><span
                                                                                                                            data-custom-class="body_text"></span></span>
                                                                                                                </bdt>
                                                                                                                </li></ul>
                                                                                                                <div style="line-height: 1.5;">
                                                                                                                    <bdt class="block-component">
                                                                                                                        <span style="font-size: 15px;"><span
                                                                                                                                data-custom-class="body_text">
                                                                                                                    </bdt>
                                                                                                                    </span></span></li></ul>
                                                                                                                    <div style="line-height: 1.5;">
                                                                                                                        <bdt class="block-component">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"></span></span>
                                                                                                                        </bdt>
                                                                                                                        </li></ul>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <bdt class="block-component">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <strong><span
                                                                                                                                    id="3pwebsites"
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="heading_1">5. WHAT IS OUR STANCE ON THIRD-PARTY WEBSITES?</span></span></strong>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><strong><em>In Short:</em></strong><em> We are not responsible for the safety of any information that you share with third parties that we may link to or who advertise on our Services, but are not affiliated with, our Services.</em></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text">The Services<bdt
                                                                                                                                    class="block-component"></bdt> may link to third-party websites, online services, or mobile applications and/or contain advertisements from third parties that are not affiliated with us and which may link to other websites, services, or applications. Accordingly, we do not make any guarantee regarding any such third parties, and we will not be liable for any loss or damage caused by the use of such third-party websites, services, or applications. The inclusion of a link towards a third-party website, service, or application does not imply an endorsement by us. We cannot guarantee the safety and privacy of data you provide to any third parties. Any data collected by third parties is not covered by this privacy notice. We are not responsible for the content or privacy and security practices and policies of any third parties, including other websites, services, or applications that may be linked to or from the Services. You should review the policies of such third parties and contact them directly to respond to your questions.</span></span>
                                                                                                                            <bdt class="statement-end-if-in-editor">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                            <span style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="block-component"><span
                                                                                                                                    data-custom-class="heading_1"></span></bdt></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="cookies"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">6. DO WE USE COOKIES AND OTHER TRACKING TECHNOLOGIES?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><em>In Short:</em></strong><em> We may use cookies and other tracking technologies to collect and store your information.</em></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">We may use cookies and similar tracking technologies (like web beacons and pixels) to access or store information. Specific information about how we use such technologies and how you can refuse certain cookies is set out in our Cookie Notice<span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt>.</span><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span></span></span></span></span></span></span></span><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt></span><bdt
                                                                                                                                    class="block-component"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span></span></span></span></span></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="inforetain"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">7. HOW LONG DO WE KEEP YOUR INFORMATION?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><em>In Short: </em></strong><em>We keep your information for as long as necessary to <bdt
                                                                                                                                    class="block-component"></bdt>fulfil<bdt
                                                                                                                                    class="else-block"></bdt> the purposes outlined in this privacy notice unless otherwise required by law.</em></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">We will only keep your personal information for as long as it is necessary for the purposes set out in this privacy notice, unless a longer retention period is required or permitted by law (such as tax, accounting, or other legal requirements).<bdt
                                                                                                                                    class="block-component"></bdt> No purpose in this notice will require us keeping your personal information for longer than <span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt></span></span> </span> <bdt
                                                                                                                                    class="block-component"></bdt>the period of time in which users have an account with us<bdt
                                                                                                                                    class="block-component"></bdt><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="else-block"></bdt></span></span></span>.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">When we have no ongoing legitimate business need to process your personal information, we will either delete or <bdt
                                                                                                                                    class="block-component"></bdt>anonymise<bdt
                                                                                                                                    class="else-block"></bdt> such information, or, if this is not possible (for example, because your personal information has been stored in backup archives), then we will securely store your personal information and isolate it from any further processing until deletion is possible.<span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="infosafe"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">8. HOW DO WE KEEP YOUR INFORMATION SAFE?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><em>In Short: </em></strong><em>We aim to protect your personal information through a system of <bdt
                                                                                                                                    class="block-component"></bdt>organisational<bdt
                                                                                                                                    class="else-block"></bdt> and technical security measures.</em></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">We have implemented appropriate and reasonable technical and <bdt
                                                                                                                                    class="block-component"></bdt>organisational<bdt
                                                                                                                                    class="else-block"></bdt> security measures designed to protect the security of any personal information we process. However, despite our safeguards and efforts to secure your information, no electronic transmission over the Internet or information storage technology can be guaranteed to be 100% secure, so we cannot promise or guarantee that hackers, cybercriminals, or other <bdt
                                                                                                                                    class="block-component"></bdt>unauthorised<bdt
                                                                                                                                    class="else-block"></bdt> third parties will not be able to defeat our security and improperly collect, access, steal, or modify your information. Although we will do our best to protect your personal information, transmission of personal information to and from our Services is at your own risk. You should only access the Services within a secure environment.<span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="privacyrights"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">9. WHAT ARE YOUR PRIVACY RIGHTS?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><em>In Short:</em></strong><em> <span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><em><bdt
                                                                                                                                    class="block-component"></bdt></em></span></span></span>In some regions, such as <bdt
                                                                                                                                    class="block-component"></bdt>the European Economic Area (EEA), United Kingdom (UK), and Switzerland<bdt
                                                                                                                                    class="block-component"></bdt>, you have rights that allow you greater access to and control over your personal information.<span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><em><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></em></span></span> </span>You may review, change, or terminate your account at any time.</em><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">In some regions (like <bdt
                                                                                                                                    class="block-component"></bdt>the EEA, UK, and Switzerland<bdt
                                                                                                                                    class="block-component"></bdt>), you have certain rights under applicable data protection laws. These may include the right (i) to request access and obtain a copy of your personal information, (ii) to request rectification or erasure; (iii) to restrict the processing of your personal information; (iv) if applicable, to data portability; and (v) not to be subject to automated decision-making. In certain circumstances, you may also have the right to object to the processing of your personal information. You can make such a request by contacting us by using the contact details provided in the section <bdt
                                                                                                                                    class="block-component"></bdt>'<bdt
                                                                                                                                    class="else-block"></bdt></span></span></span><a
                                                                                                                                data-custom-class="link"
                                                                                                                                href="#contact"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                data-custom-class="body_text">HOW CAN YOU CONTACT US ABOUT THIS NOTICE?</span></span></span></a><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                data-custom-class="body_text"><bdt
                                                                                                                                class="block-component"></bdt>'<bdt
                                                                                                                                class="else-block"></bdt> below.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">We will consider and act upon any request in accordance with applicable data protection laws.<bdt
                                                                                                                                    class="block-component"></bdt></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"> </span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">If you are located in the EEA or UK and you believe we are unlawfully processing your personal information, you also have the right to complain to your <span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><a
                                                                                                                                    data-custom-class="link"
                                                                                                                                    href="https://ec.europa.eu/justice/data-protection/bodies/authorities/index_en.htm"
                                                                                                                                    rel="noopener noreferrer"
                                                                                                                                    target="_blank"><span
                                                                                                                                    style="font-size: 15px;">Member State data protection authority</span></a></span></span></span></span></span> or </span></span></span><a
                                                                                                                                data-custom-class="link"
                                                                                                                                href="https://ico.org.uk/make-a-complaint/data-protection-complaints/data-protection-complaints/"
                                                                                                                                rel="noopener noreferrer"
                                                                                                                                target="_blank"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                data-custom-class="body_text">UK data protection authority</span></span></span></a><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                data-custom-class="body_text">.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">If you are located in Switzerland, you may contact the <span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(0, 58, 250); font-size: 15px;"><a
                                                                                                                                    data-custom-class="link"
                                                                                                                                    href="https://www.edoeb.admin.ch/edoeb/en/home.html"
                                                                                                                                    rel="noopener noreferrer"
                                                                                                                                    target="_blank">Federal Data Protection and Information Commissioner</a></span></span></span></span></span></span>.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="withdrawconsent"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><u>Withdrawing your consent:</u></strong> If we are relying on your consent to process your personal information,<bdt
                                                                                                                                    class="block-component"></bdt><bdt
                                                                                                                                    class="else-block"></bdt> you have the right to withdraw your consent at any time. You can withdraw your consent at any time by contacting us by using the contact details provided in the section <bdt
                                                                                                                                    class="block-component"></bdt>'<bdt
                                                                                                                                    class="else-block"></bdt></span></span></span><a
                                                                                                                                data-custom-class="link"
                                                                                                                                href="#contact"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                style="font-size: 15px; color: rgb(0, 58, 250);"><span
                                                                                                                                data-custom-class="body_text">HOW CAN YOU CONTACT US ABOUT THIS NOTICE?</span></span></span></a><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                data-custom-class="body_text"><bdt
                                                                                                                                class="block-component"></bdt>'<bdt
                                                                                                                                class="else-block"></bdt> below<bdt
                                                                                                                                class="block-component"></bdt>.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text">However, please note that this will not affect the lawfulness of the processing before its withdrawal nor,<bdt
                                                                                                                                    class="block-component"></bdt><bdt
                                                                                                                                    class="else-block"></bdt> will it affect the processing of your personal information conducted in reliance on lawful processing grounds other than consent.<bdt
                                                                                                                                    class="block-component"></bdt></span></span>
                                                                                                                            <bdt class="block-component">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="heading_2"><strong>Account Information</strong></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;">If you would at any time like to review or change the information in your account or terminate your account, you can:<bdt
                                                                                                                                    class="forloop-component"></bdt></span></span>
                                                                                                                        </div>
                                                                                                                        <ul>
                                                                                                                            <li style="line-height: 1.5;">
                                                                                                                                <span data-custom-class="body_text"><span
                                                                                                                                        style="font-size: 15px;"><bdt
                                                                                                                                        class="question">Log in to your account settings and update your user account.</bdt></span></span>
                                                                                                                            </li>
                                                                                                                        </ul>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><bdt
                                                                                                                                    class="forloop-component"></bdt></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text">Upon your request to terminate your account, we will deactivate or delete your account and information from our active databases. However, we may retain some information in our files to prevent fraud, troubleshoot problems, assist with any investigations, enforce our legal terms and/or comply with applicable legal requirements.</span></span>
                                                                                                                            <bdt class="statement-end-if-in-editor">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span></span></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><strong><u>Cookies and similar technologies:</u></strong> Most Web browsers are set to accept cookies by default. If you prefer, you can usually choose to set your browser to remove cookies and to reject cookies. If you choose to remove cookies or reject cookies, this could affect certain features or services of our Services. <bdt
                                                                                                                                    class="block-component"></bdt>You may also <span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><a
                                                                                                                                    data-custom-class="link"
                                                                                                                                    href="http://www.aboutads.info/choices/"
                                                                                                                                    rel="noopener noreferrer"
                                                                                                                                    target="_blank"><span
                                                                                                                                    style="color: rgb(0, 58, 250); font-size: 15px;">opt out of interest-based advertising by advertisers</span></a></span></span> on our Services. <span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span></span></span></span></span></span></span></span></span></span></span></span>
                                                                                                                            <bdt class="block-component">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;">If you have questions or comments about your privacy rights, you may email us at <bdt
                                                                                                                                    class="question">kacperwlodarczyk@protonmail.com</bdt>.</span></span>
                                                                                                                            <bdt class="statement-end-if-in-editor">
                                                                                                                                <span style="font-size: 15px;"><span
                                                                                                                                        data-custom-class="body_text"></span></span>
                                                                                                                            </bdt>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="DNT"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">10. CONTROLS FOR DO-NOT-TRACK FEATURES</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">Most web browsers and some mobile operating systems and mobile applications include a Do-Not-Track (<bdt
                                                                                                                                    class="block-component"></bdt>'DNT'<bdt
                                                                                                                                    class="else-block"></bdt>) feature or setting you can activate to signal your privacy preference not to have data about your online browsing activities monitored and collected. At this stage no uniform technology standard for <bdt
                                                                                                                                    class="block-component"></bdt>recognising<bdt
                                                                                                                                    class="else-block"></bdt> and implementing DNT signals has been <bdt
                                                                                                                                    class="block-component"></bdt>finalised<bdt
                                                                                                                                    class="else-block"></bdt>. As such, we do not currently respond to DNT browser signals or any other mechanism that automatically communicates your choice not to be tracked online. If a standard for online tracking is adopted that we must follow in the future, we will inform you about that practice in a revised version of this privacy notice.<bdt
                                                                                                                                    class="block-component"></bdt>
                                                                                                                                </bdt></span></span></span></span></span></span></span></span></span></span></span></bdt></span></span></span></span></span></span></span></span></span></span>
                                                                                                                            <bdt class="block-component">
                                                                                                                                <span style="font-size: 15px;">
                                                                                                                            </bdt>
                                                                                                                            </span>
                                                                                                                            <bdt class="block-component">
                                                                                                                                <span style="font-size: 15px;"></span>
                                                                                                                            </bdt>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="policyupdates"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">11. DO WE MAKE UPDATES TO THIS NOTICE?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><em><strong>In Short: </strong>Yes, we will update this notice as necessary to stay compliant with relevant laws.</em></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">We may update this privacy notice from time to time. The updated version will be indicated by an updated <bdt
                                                                                                                                    class="block-component"></bdt>'Revised'<bdt
                                                                                                                                    class="else-block"></bdt> date and the updated version will be effective as soon as it is accessible. If we make material changes to this privacy notice, we may notify you either by prominently posting a notice of such changes or by directly sending you a notification. We encourage you to review this privacy notice frequently to be informed of how we are protecting your information.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="contact"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">12. HOW CAN YOU CONTACT US ABOUT THIS NOTICE?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">If you have questions or comments about this notice, you may <span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"><bdt
                                                                                                                                    class="block-component"></bdt></bdt>email us at <bdt
                                                                                                                                    class="question">kacperwlodarczyk@protonmail.com or </bdt><bdt
                                                                                                                                    class="statement-end-if-in-editor"><bdt
                                                                                                                                    class="block-component"></bdt></bdt></span></span><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text">contact us by post at:</span></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="question">FJob</bdt></span></span></span></span></span><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt>
                                                                                                                                </bdt></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="question">__________</bdt><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></bdt></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="question">Łódź</bdt><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><bdt
                                                                                                                                    class="block-component"></bdt>, <bdt
                                                                                                                                    class="question">łódzkie</bdt><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt><bdt
                                                                                                                                    class="block-component"></bdt><bdt
                                                                                                                                    class="block-component"></bdt><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></bdt></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span><bdt
                                                                                                                                    class="question">Poland</bdt><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span></span></span></bdt><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span></span></span><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><bdt
                                                                                                                                    class="statement-end-if-in-editor"></bdt></span></span></span></bdt></span></span></span></span><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><bdt
                                                                                                                                    class="statement-end-if-in-editor"><span
                                                                                                                                    style="color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"><bdt
                                                                                                                                    class="block-component"></bdt></span></span></span></span></span></span><bdt
                                                                                                                                    class="block-component"><span
                                                                                                                                    style="font-size: 15px;"></span></bdt><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px;"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="statement-end-if-in-editor"><bdt
                                                                                                                                    class="block-component"></bdt></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div id="request"
                                                                                                                             style="line-height: 1.5;">
                                                                                                                            <span style="color: rgb(127, 127, 127);"><span
                                                                                                                                    style="color: rgb(89, 89, 89); font-size: 15px;"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    id="control"
                                                                                                                                    style="color: rgb(0, 0, 0);"><strong><span
                                                                                                                                    data-custom-class="heading_1">13. HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?</span></strong></span></span></span></span></span>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <br>
                                                                                                                        </div>
                                                                                                                        <div style="line-height: 1.5;">
                                                                                                                            <span style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    style="font-size: 15px; color: rgb(89, 89, 89);"><span
                                                                                                                                    data-custom-class="body_text"><bdt
                                                                                                                                    class="block-component"></bdt>Based on the applicable laws of your country, you may have the right to request access to the personal information we collect from you, change that information, or delete it. <bdt
                                                                                                                                    class="else-block"><bdt
                                                                                                                                    class="block-component"></bdt>To request to review, update, or delete your personal information, please <bdt
                                                                                                                                    class="block-component"></bdt>fill out and submit a </span><span
                                                                                                                                    style="color: rgb(0, 58, 250);"><span
                                                                                                                                    data-custom-class="body_text"><span
                                                                                                                                    style="color: rgb(0, 58, 250); font-size: 15px;"><a
                                                                                                                                    data-custom-class="link"
                                                                                                                                    href="https://app.termly.io/notify/e4effab4-134f-44f5-ab80-0c1566c85de2"
                                                                                                                                    rel="noopener noreferrer"
                                                                                                                                    target="_blank">data subject access request</a></span></span></span><bdt
                                                                                                                                    class="block-component"><span
                                                                                                                                    data-custom-class="body_text"></bdt></span></span><span
                                                                                                                                data-custom-class="body_text">.</span></span></span>
                                                                                                                        </div>
                                                                                                                        <style>
                                                                                                                            ul {
                                                                                                                                list-style-type: square;
                                                                                                                            }

                                                                                                                            ul > li > ul {
                                                                                                                                list-style-type: circle;
                                                                                                                            }

                                                                                                                            ul > li > ul > li > ul {
                                                                                                                                list-style-type: square;
                                                                                                                            }

                                                                                                                            ol li {
                                                                                                                                font-family: Arial;
                                                                                                                            }
                                                                                                                        </style>
                                                                                                                    </div>
                                                                                                                    <div style="color: #595959;font-size: 14px;font-family: Arial;padding-top:16px;">
                                                                                                                        This
                                                                                                                        privacy
                                                                                                                        policy
                                                                                                                        was
                                                                                                                        created
                                                                                                                        using
                                                                                                                        Termly's
                                                                                                                        <a style="color: rgb(48, 48, 241) !important;"
                                                                                                                           href="https://termly.io/products/privacy-policy-generator/">Privacy
                                                                                                                            Policy
                                                                                                                            Generator</a>.
                                                                                                                    </div>`;


const mySafeHTML = DOMPurify.sanitize(myHTML);


export const PrivatePolicyPage = () => <div dangerouslySetInnerHTML={{__html: mySafeHTML}}/>;