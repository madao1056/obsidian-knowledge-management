---
notion_id: 440ad0aa-6bf4-4782-8f55-9740bfacc4ef
account: Secondary
title: Smart Custom Fields（SCF）
url: https://www.notion.so/Smart-Custom-Fields-SCF-440ad0aa6bf447828f559740bfacc4ef
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.507326
---
# Smart Custom Fields（SCF）

  画像以外のカスタムフィールド（リンク、テキスト、タイトルなど）は必要に応じて入れて下さい。
  ```php
<!-- 画像を含む場合(同一フィールド) -->
<ul class="">
  <?php
    $repeat_item = SCF::get('グループ名');
    foreach ($repeat_item as $fields ) {
    $image_url = wp_get_attachment_image_src($fields['画像用のフィールド名'] , 'full');
  ?>
  <li class="">
    <a href="<?php echo $fields["リンク用のフィールド名"]; ?>" class="">
      <div>
        <img src="<?php echo $image_url[0]; ?>" width="<?php echo $image_url[1]; ?>"
          height="<?php echo $image_url[2]; ?>" alt="<?php echo $fields["altタグ用のフィールド名)"]; ?>">
      </div>
      <div>
        <?php echo $fields['テキストやタイトルなどのフィールド名']; ?>
      </div>
    </a>
  </li>
  <?php } ?>
</ul>
  ```
  
  ```php
<!-- 画像が2種類ある場合(同一フィールド) -->
<ul class="">
  <?php
    $repeat_item = SCF::get('グループ名');
    foreach ($repeat_item as $fields ) {
    $image_url_first = wp_get_attachment_image_src($fields['画像用のフィールド名1'] , 'full');
		$image_url_second = wp_get_attachment_image_src($fields['画像用のフィールド名2'] , 'full');
  ?>
  <li class="">
    <a href="<?php echo $fields["リンク用のフィールド名"]; ?>" class="">
      <div>
        <img src="<?php echo $image_url_first[0]; ?>" width="<?php echo $image_url_first[1]; ?>"
          height="<?php echo $image_url_first[2]; ?>" alt="<?php echo $fields["altタグ用のフィールド名1)"]; ?>">
      </div>
			<div>
        <img src="<?php echo $image_url_second[0]; ?>" width="<?php echo $image_url_second[1]; ?>"
          height="<?php echo $image_url_second[2]; ?>" alt="<?php echo $fields["altタグ用のフィールド名2)"]; ?>">
      </div>
      <div>
        <?php echo $fields['テキストやタイトルなどのフィールド名']; ?>
      </div>
    </a>
  </li>
  <?php } ?>
</ul>
  ```
  
  ```php
<?php
  $repeat_item = SCF::get('グループ名');
  foreach ($repeat_item as $fields) { 
?>
<?php echo $fields['フィールド名']; ?>
<?php } ?>
  ```
  
  ```php
<!-- 繰り返しの場合 -->
<?php echo nl2br($fields['フィールド名']); ?>

<!-- 繰り返しじゃない場合 -->
<?php
  $textarea = SCF::get('フィールド名');
  echo nl2br($textarea);
?>
  ```
  
  ```php
//Smart Custom Fieldsのオプション繰り返し(functions.php)
  /**
   * @param string $page_title ページのtitle属性値
   * @param string $menu_title 管理画面のメニューに表示するタイトル
   * @param string $capability メニューを操作できる権限（manage_options とか）
   * @param string $menu_slug オプションページのスラッグ。ユニークな値にすること。
   * @param string|null $icon_url メニューに表示するアイコンの URL
   * @param int $position メニューの位置
   */
  SCF::add_options_page( 'ページタイトル', 'メニュータイトル', 'manage_options', 'theme-options' );
  ```
  ```php
<!-- ページテンプレート(header.phpなど) -->
<ul class="">
  <?php
    $repeat_item = SCF::get_option_meta( 'theme-options', 'フィールドグループ名' );
    foreach ( $repeat_item as $field_name => $field_value ) {
  ?>
  <li class="">
    <a href="" class="">
			<?php echo esc_html( $field_value['フィールド名'] ); ?>
		</a>
  </li>
  <?php } ?>
</ul>
  ```
  詳細は以下の記事を参照
  [Bookmark](https://junpei-sugiyama.com/smart-custom-fields-common/)
  ```php
<?php
  $repeat_item = SCF::get('グループ名');
  foreach ($repeat_item as $fields ) {
  $file = wp_get_attachment_url($fields['ファイルのフィールド名']);
?>
<!-- これでファイルを出力 -->
<a href="<?php echo $file; ?>" target="_blank" rel="noopener noreferrer">
  <?php echo $fields['ファイル名のフィールド名']; ?>
</a>
<?php } ?>
  ```
  ファイルはURLで出力されるのでaタグのhrefに入れておき、別タブで開くように設定すればOK。
  あとはファイル名を出力するカスタムフィールドを設定しておくとファイル名も自由に編集可能。
  ```php
<!-- 繰り返す場合 -->
<?php
  $repeat_item = SCF::get('グループ名');
  foreach ($repeat_item as $fields) {
  $check_item = $fields['フィールド名'];
?>
<ul class="">
  <?php
    $repeat_item = SCF::get('グループ名');
    foreach ($check_item as $field) {
  ?>
  <li class="">
    <?php echo $field; ?>
  </li>
  <?php } ?>
</ul>
<?php } ?>

<!-- 繰り返さない場合 -->
<ul class="">
  <?php
	  $checkbox = SCF::get('フィールド名');
	  foreach ($checkbox as $field) {
	?>
  <li class="">
    <?php echo $field; ?>
  </li>
  <?php } ?>
</ul>
  ```
  
  ```php
<!-- 繰り返す場合 -->
<div>
  <?php
    $repeat_item = SCF::get('グループ名');
    foreach ($repeat_item as $fields ) {
  ?>
  <div>
    <?php
      foreach ($fields as $field) {
    ?>
    <?php if( $field == '選択肢1' ): ?>
	    選択肢1が選択された時に表示する内容
    <?php elseif( $field == '選択肢2' ): ?>
	    選択肢2が選択された時に表示する内容
    <?php elseif( $field == '選択肢3' ): ?>
	    選択肢3が選択された時に表示する内容
    <?php endif; ?>
    <?php } ?>
  </div>
  <?php } ?>
</div>

<!-- 繰り返さない場合 -->
<div class="">
	<?php $field = SCF::get('フィールド名'); ?>
	<?php if( $field == '選択肢1' ): ?>
		選択肢1が選択された時に表示する内容
	<?php elseif( $field == '選択肢2' ): ?>
		選択肢2が選択された時に表示する内容
	<?php elseif( $field == '選択肢3' ): ?>
		選択肢3が選択された時に表示する内容
	<?php endif; ?>
</div>
  ```
  
  SCFの編集画面が以下の場合、ページの編集画面とコードは次のようになります（繰り返し）
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/b8515bc7-f8a4-4439-9961-00c4568378ae/SCF1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTM7LYIY%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T061004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvwMNJBe4iHfvXDFxGQxlP5b%2FPJRTm2zjMRBrfNtQ3PgIhANPp8dtmwhUch%2F7U24pcNnw6AQzh4EJSEWqOozc8J3hkKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw00DA0UIYNcAmCPTEq3ANTVWRVZ5iDNuFHfMg6fMOr673lAXoTzZ8ebiJi9Z8VeAquM31uBsDh7kC5VAqJ2vf9FvroOwaOuzxtg4JP1ScVDgobu8j331hBw64eM1p7Tb%2FC8liUHRBQafaGOMxFJ4qbN3vXzDnUbJXq6GwoGsNlJR6Wv5HkbFRNw8NdZ2gTzUB1RzvVGrM0u6GaGvWkSGFgc6XK63lrRkyKggArkTWFcAHg0nDbIpOCqGzFd8S0dXK0fIY%2FD3e1xualakPTQz792Hp2Kd%2BiCyov6iHdOcPGy6qgg2oCaafTIUDaLyo23t%2FWV%2FaZ02irUolkrGUZeGD5QjK6yTjLMPKqRtJLHMdIHgkQvXaid860Pd4KMHHRpmtIaa0S%2B459AwwkriNiMAzecvl7LqvxPtYLa%2BhF0Dq6NcPHDahbhOMGxeMXLzrwh5HRw9uD96ED4ZckZ2WIKFr97Q3S%2B2X3GopD5eQ6Gsq5a25cuBUSqHUc7ifNQvQSSie0VSeeDy%2Bd7I4lf%2FPt74uTE1I%2FPCZT4Vl8wHpQPPG84AXHpkbo2hf3ItxvEZ0FWxGf%2B%2B2WeEHkkO%2B3xNHT0VqTS7G178fEHI5DJ4m4rd3sn1QZtJkX81EbG7Qtvd1rrzER7UNxIfNj3xwWETCIxezDBjqkASeIBD0yGqrPHEMJo9yWGOB6Qtht%2FbQfK1RxzXBMQEuZBsEI9b%2BRpnS6tyesG%2BCey%2FeZTogPRajs%2FATl1aDPMPgZ5jdVkZl6FLoQLX8POiY9XNLznspNSXn6oJGyxCGfdXH5GDPj1jP59V6r7k%2B0TSs7q9r6N1Y9yjJUXNOsJrLRSTOQqMtQexjilSsWGiJUJprX2kbDouzEOi3pA4clC7ip5a48&X-Amz-Signature=db80932edd073ab33f832f944d80771a0243a02c1c43257b52298c32c4760eff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  これがページの編集画面（SCFは項目を増やしたり減らしたりが無料で可能）
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/3408528f-bcef-42df-bd26-9100380b6719/SCF2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTM7LYIY%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T061004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvwMNJBe4iHfvXDFxGQxlP5b%2FPJRTm2zjMRBrfNtQ3PgIhANPp8dtmwhUch%2F7U24pcNnw6AQzh4EJSEWqOozc8J3hkKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw00DA0UIYNcAmCPTEq3ANTVWRVZ5iDNuFHfMg6fMOr673lAXoTzZ8ebiJi9Z8VeAquM31uBsDh7kC5VAqJ2vf9FvroOwaOuzxtg4JP1ScVDgobu8j331hBw64eM1p7Tb%2FC8liUHRBQafaGOMxFJ4qbN3vXzDnUbJXq6GwoGsNlJR6Wv5HkbFRNw8NdZ2gTzUB1RzvVGrM0u6GaGvWkSGFgc6XK63lrRkyKggArkTWFcAHg0nDbIpOCqGzFd8S0dXK0fIY%2FD3e1xualakPTQz792Hp2Kd%2BiCyov6iHdOcPGy6qgg2oCaafTIUDaLyo23t%2FWV%2FaZ02irUolkrGUZeGD5QjK6yTjLMPKqRtJLHMdIHgkQvXaid860Pd4KMHHRpmtIaa0S%2B459AwwkriNiMAzecvl7LqvxPtYLa%2BhF0Dq6NcPHDahbhOMGxeMXLzrwh5HRw9uD96ED4ZckZ2WIKFr97Q3S%2B2X3GopD5eQ6Gsq5a25cuBUSqHUc7ifNQvQSSie0VSeeDy%2Bd7I4lf%2FPt74uTE1I%2FPCZT4Vl8wHpQPPG84AXHpkbo2hf3ItxvEZ0FWxGf%2B%2B2WeEHkkO%2B3xNHT0VqTS7G178fEHI5DJ4m4rd3sn1QZtJkX81EbG7Qtvd1rrzER7UNxIfNj3xwWETCIxezDBjqkASeIBD0yGqrPHEMJo9yWGOB6Qtht%2FbQfK1RxzXBMQEuZBsEI9b%2BRpnS6tyesG%2BCey%2FeZTogPRajs%2FATl1aDPMPgZ5jdVkZl6FLoQLX8POiY9XNLznspNSXn6oJGyxCGfdXH5GDPj1jP59V6r7k%2B0TSs7q9r6N1Y9yjJUXNOsJrLRSTOQqMtQexjilSsWGiJUJprX2kbDouzEOi3pA4clC7ip5a48&X-Amz-Signature=bb1d11778fac9e81d5881ca6a63aa73163e0b72984a331e974a72f64d29b5d1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  表示する内容はテキストや画像など何でもOK
  ```php
<!-- 繰り返す場合 -->
<div>
  <?php
    $repeat_item = SCF::get('dog-info');
    foreach ($repeat_item as $fields ) {
  ?>
  <div>
    <?php
      foreach ($fields as $field) {
    ?>
    <?php if( $field == '大型犬' ): ?>
	    大型犬が選択された時に表示する内容
    <?php elseif( $field == '中型犬' ): ?>
	    中型犬が選択された時に表示する内容
    <?php elseif( $field == '小型犬' ): ?>
	    小型犬が選択された時に表示する内容
    <?php endif; ?>
    <?php } ?>
  </div>
  <?php } ?>
</div>

<!-- 繰り返さない場合 -->
<div class="">
	<?php $field = SCF::get('dog-size'); ?>
	<?php if( $field == '大型犬' ): ?>
		大型犬が選択された時に表示する内容
	<?php elseif( $field == '中型犬' ): ?>
		中型犬が選択された時に表示する内容
	<?php elseif( $field == '小型犬' ): ?>
		小型犬が選択された時に表示する内容
	<?php endif; ?>
</div>
  ```
  ```php
<?php
  $field = SCF::get('フィールド名');
  echo nl2br($field);
?>
  ```
  
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/46a3dbf4-c98e-4e66-9998-4fea9d3d302d/SCF.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFX5DSFB%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYF1gWz1D%2B1fM76M%2F3FfNVbmmZh6rxe0l1sxoiOnbdWwIhAOF28VuaK3aUrY3WIY0m%2FAJjz6ukNX%2BF0vjqMYJXeA8KKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcBx2Of8FpiP%2FHO2Mq3ANRa%2FnFWDsvZsji7uiFv5LC9RTbNX2hHz7Oijq7NFIzhFRcF2a6Bpqavyah7QiuyucP072ygs238Gtw7jm80FimLgtICAj5%2F3ZENykzJU%2FDFbZCPkICnQ0EYzmB9dgqPkm3iubq6AzPLvQX2pSoSn2QB28Xr7xOofrPhdGS3m3El5wg4O0K1EMLQIOMPinyRyOwYNDxL8OtndAYllr0hqYDEnGwzASt0HlUG1XOzaySTALJx2O2IdffBQ05AoR8LafuZL2IveprRDXDbqgQUO5xPFR3Eyne5ZVmbgDeN9tYxVGHkZLrNVsbfKd5rcso6x8a46HvmczjbPGzrWFFXonGpLsdNSWa8GDjPJx9vx8zMGlHpnJkV7d8XhWn5i4hfmZmuGrVXak58u7p5th4jz4wFh8V%2FbMVzsAxt5rB2JXFN%2BH%2FgeC%2Ft8JMDRst%2F%2B%2F%2FLKDlmzJHXo%2BTJv%2BtgThoi%2FIBnjtneG2aMEQhsMPwpJZdW8BoWzk%2FVbLUPW%2F%2FzvH7z%2BC5dKb9Ppc9O%2BxJV%2Fdurmo865gENsKgaZNMle4FffRYGRKLYmRoatj0EpXIlT%2FqwQwz%2BMhw5Ouzjd2xI2k7wajt0itmiU8Fc1NTvx6mUF9uxqz1owzPVQAr66xJgDCExuzDBjqkASzEYL07xKD92dQCCyBG%2B%2F7GaAU6TaGLrUsmlaB2NhTgqsKWm9HjaTkBsjHoucjIIrdUtFoxexjD3ab6EYZ6yevEv%2ByblUr%2BevIHJkEHrxcrFnEeH0iVk5OBy8ttaW5vvGKWLXE%2BMU8IfEqV1u6LaJ88AutjoXVCxbr6%2Bkeaj4U1U8XIc6ki475X56KRGzjmPwFEZSsxpeR3O98Ck5ITVkVd94wB&X-Amz-Signature=bbf2b1294f657ff20c4b761f308b485dd5c1b569da213c7ac6f08cf62859e322&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)