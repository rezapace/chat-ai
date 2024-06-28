// src/ChatApp.tsx
import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './ChatApp.css';

interface Message {
  role: 'user' | 'gemini' | 'groq';
  content: string;
}

const ChatApp: React.FC = () => {
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const handleChat = async () => {
    if (!prompt.trim()) return;

    const userMessage: Message = { role: 'user', content: prompt };
    setMessages(prev => [...prev, userMessage]);
    setPrompt('');

    try {
      const response = await axios.post('http://localhost:5000/chat', {
        prompt_gemini: prompt,
        prompt_groq: prompt,
      });

      const geminiMessage: Message = { role: 'gemini', content: response.data.gemini_response };
      const groqMessage: Message = { role: 'groq', content: response.data.groq_response };

      setMessages(prev => [...prev, geminiMessage, groqMessage]);
    } catch (error) {
      console.error('Error fetching chat responses:', error);
    }
  };

  return (
    <div className="chat-app">
      <header className="app-header">
        <h1>AI Chat Comparison</h1>
        <p>Compare responses from Gemini and Groq</p>
      </header>
      <div className="chat-container">
        <div className="chat-messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.role}`}>
              {message.role !== 'user' && <div className="message-role">{message.role}</div>}
              <div className="message-content">{message.content}</div>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>
        <div className="chat-input">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleChat();
              }
            }}
            placeholder="Type your message here..."
          />
          <button onClick={handleChat}>Send</button>
        </div>
      </div>
    </div>
  );
};

export default ChatApp;
