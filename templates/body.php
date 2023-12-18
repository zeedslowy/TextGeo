<?php
    // Update the path below to your autoload.php,
    // see https://getcomposer.org/doc/01-basic-usage.md
    require_once '/path/to/vendor/autoload.php';
    use Twilio\Rest\Client;

    $sid    = "ACa7654efe0b72d001e50da95684127cc2";
    $token  = "[AuthToken]";
    $twilio = new Client($sid, $token);

    $message = $twilio->messages
      ->create("+905449096348", // to
        array(
          "from" => "+12058943188",
          "body" => "Your Message"
        )
      );

print($message->sid);
