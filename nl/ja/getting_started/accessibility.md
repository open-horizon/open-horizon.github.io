---

copyright:
  years: 2016, 2019
lastupdated: "2019-03-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# アクセシビリティー機能

アクセシビリティー機能は、運動障がいまたは視覚障がいなどの身体障がいを持つユーザーが情報技術コンテンツを快適に使用できるようにサポートします。
{:shortdesc}

## 概要

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) には、以下の主なアクセシビリティー機能が含まれています。

* キーボードのみでの操作
* スクリーン・リーダーでの操作
* {{site.data.keyword.ieam}} クラスターを管理するためのコマンド・ライン・インターフェース (CLI)

{{site.data.keyword.ieam}} では、最新の W3C 標準である [WAI-ARIA 1.0 ![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")](http://www.w3.org/TR/wai-aria/){: new_window} を使用して、[Section 508 Standards for Electronic and Information Technology ![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards){: new_window} および [Web Content Accessibility Guidelines (WCAG) 2.0 ![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")](http://www.w3.org/TR/WCAG20/){: new_window}に対する準拠を確保しています。 アクセシビリティー機能を利用するには、スクリーン・リーダーの最新リリースおよび {{site.data.keyword.ieam}} でサポートされる最新の Web ブラウザーを使用してください。

IBM 資料の {{site.data.keyword.ieam}} のオンライン製品資料は、アクセシビリティー対応です。 一般的なアクセシビリティーの情報については、[IBM におけるアクセシビリティー ![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")](http://www.ibm.com/accessibility/jp/ja/){: new_window}を参照してください。

## ハイパーリンク

すべての外部リンク (IBM 資料の外部でホストされているコンテンツへのリンク) は、新規ウィンドウで開きます。 このような外部リンクには、外部リンク・アイコン (![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")) によるフラグも立てられています。

## キーボード・ナビゲーション

{{site.data.keyword.ieam}} では、標準ナビゲーション・キーを使用します。

{{site.data.keyword.ieam}} では、以下のキーボード・ショートカットを使用します。

|アクション|Internet Explorer のショートカット|Firefox のショートカット|
|------|------------------------------|--------------------|
|コンテンツ・ビュー・フレームに移動|Alt+C の後に、Enter および Shift+F6 を押す|Shift+Alt+C および Shift+F6|
{: caption="表 1. {{site.data.keyword.ieam}} でのキーボード・ショートカット" caption-side="top"}

## インターフェース情報

{{site.data.keyword.ieam}} では、スクリーン・リーダーの最新バージョンを使用してください。

{{site.data.keyword.ieam}} ユーザー・インターフェースには、1 秒間に 2 から 55 回点滅するコンテンツは含まれていません。

{{site.data.keyword.ieam}} Web ユーザー・インターフェースでは、コンテンツを適切にレンダリングするため、および使いやすい使用感を提供するために、カスケーディング・スタイル・シートを利用しています。 このアプリケーションでは、ハイコントラスト・モードなど、低視力のユーザーがシステム表示設定を使用するための同等の手段が用意されています。 デバイスまたは Web ブラウザーの設定を使用して、フォント・サイズを制御できます。

{{site.data.keyword.gui}} にアクセスするには、Web ブラウザーを開き、以下の URL にナビゲートします。

`https://<Cluster Master Host>:<Cluster Master API Port>/edge`

ユーザー名とパスワードは config.yaml ファイルで定義されます。

{{site.data.keyword.gui}} では、コンテンツを適切にレンダリングするため、および使いやすい使用感を提供するために、カスケーディング・スタイル・シートを利用することはしていません。 ただし、IBM Knowledge Documentation にある製品資料では、カスケーディング・スタイル・シートを利用しています。 {{site.data.keyword.ieam}} では、ハイコントラスト・モードなど、低視力のユーザーがシステム表示設定を使用するための同等の手段が用意されています。 デバイスまたはブラウザーの設定を使用して、フォント・サイズを制御できます。 標準スクリーン・リーダーは、製品資料に含まれているファイル・パス、環境変数、コマンド、およびその他のコンテンツの発音を間違える可能性があることに留意してください。 説明が最も正確になるようにするために、すべての句読点を読むようにスクリーン・リーダーを構成してください。


## ベンダー・ソフトウェア

{{site.data.keyword.ieam}} には、IBM のご使用条件でカバーされない特定のベンダー・ソフトウェアが含まれています。 IBM は、そうした製品のアクセシビリティー機能についていかなる表明も行いません。 各製品に関するアクセシビリティー情報については、該当するベンダーにお問い合わせください。

## 関連アクセシビリティー情報

標準 IBM ヘルプ・デスクおよびサポート Web サイトに加え、IBM では TTY 電話サービスを用意しています。このサービスは、聴覚障がいを持つお客様が販売やサポートのサービスにアクセスするためにご利用いただけます。

TTY サービス  
 800-IBM-3383 (800-426-3383)  
 (北アメリカ内)

IBM のアクセシビリティーに対する取り組みについて詳しくは、[IBM Accessibility ![外部リンク・アイコン](../images/icons/launch-glyph.svg "外部リンク・アイコン")](http://www.ibm.com/able){: new_window}を参照してください。
