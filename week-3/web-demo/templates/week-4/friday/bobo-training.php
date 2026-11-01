<?php
/**
 * Plugin Name: Bobo Training
 * Description: Training plugin for learning WordPress development.
 * Version: 0.1.0
 * Author: Bobo
 */


add_shortcode('bobo_project', 'bobo_project_shortcode');
function bobo_project_shortcode($atts,$content=null) {
    // var_dump($atts);
    // exit;

    $atts = shortcode_atts(
        [
            'color' => 'red',
            'title' => 'Project',
            'status' => 'Learning',
            'url' => 'http://localhost:8080/?page_id=24',
        ],
        $atts
    );

    $color = $atts['color'];
    $title = $atts['title'];
    $status = $atts['status'];
    $url = $atts['url'];

    if ($content == null){
        $content = 'This content came from Bobo Training plugin';
    }
    
    return '<h1 style="color:' . $color . ';">' . esc_html($title) . '</h1>' . '<p>' . esc_html($status) . '</p>' . '<p style="color:' . $color . ';">' . esc_html($content) . '</p>' . '<p>' . esc_url($url) . '</p>' ;
}
