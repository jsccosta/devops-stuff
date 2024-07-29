import { useState } from "react";
import axios from "axios";


const formatResponse = (response) => {
    const result = response.replace(/^.*\n.*\n.*.*\n.*\]\s./, '')
    return result
}

const ChatBot = () => {
    const [messages, setMessages] = useState([]);
    const [promptType, setPromptType] = useState("Question");
    const [isLoading, setIsLoading] = useState(false);

    // ToDo: configure the system message and token usage
    // Figure out how this is processed
    const sendMessage = async (prompt: string) => {
        const data = JSON.stringify({
            system_message: "You are a helpful assistant",
            user_message: prompt,
            // need to figure out if we need to actually set the number of tokens
            max_tokens: 300
        });
        const customConfig = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        try {
            setIsLoading(true);
            const response = await axios.post("/api/v1/llama", data, customConfig);
            const botReply = {
                text: formatResponse(response.data.choices[0].text),
                isBot: true,
            };
            return botReply;
        } catch (error) {
            console.error("Error:", error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleMessageSubmit = async (e) => {
        e.preventDefault();
        const messageText = e.target.elements.message.value;

        console.log({ messageText })
        if (messageText.trim() !== "") {
            const newMessage = {
                text: messageText,
                isBot: false,
            };
            setMessages([...messages, newMessage]);
            const botReply = await sendMessage(messageText);
            setMessages([...messages, newMessage, botReply]);
            e.target.elements.message.value = "";
        }
    };

    const [openChat, setOpenChat] = useState(false)

    return (
        <div className="z-1 fixed bottom-0 right-0 mb-4 mr-4">
            <button id="open-chat" className="bg-silas-dark text-white py-2 px-4 rounded-md hover:bg-silas-medium transition duration-300 flex items-center"
                onClick={() => setOpenChat(true)}
            >
                <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                </svg>
                Chat with Edward
            </button>


            <div id="chat-container" className={`${openChat ? null : 'hidden'} fixed bottom-16 right-4 w-96`}>
                <div className="bg-white shadow-md rounded-lg max-w-lg w-full">
                    <div className="p-4 border-b bg-silas-dark text-white rounded-t-lg flex justify-between items-center">
                        {/* <p className="text-lg font-semibold">Silas Bot</p> */}
                        <p className="text-lg font-semibold">Edward</p>
                        <button id="close-chat" className="text-gray-300 hover:text-gray-400 focus:outline-none focus:text-gray-400"
                            onClick={() => setOpenChat(false)}
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                        </button>
                    </div>
                    <div id="chatbox" className="p-4 h-80 overflow-y-auto">
                        {messages.map((message, index) => (
                            <>
                                {message?.isBot ? (
                                    <div key={index} className="mb-2">
                                        <p className="bg-gray-200 text-gray-700 rounded-lg py-2 px-4 inline-block">{message?.text}</p>
                                    </div>
                                ) : (
                                    <div key={index} className="mb-2 text-right">
                                        <p className="bg-silas-dark text-white rounded-lg py-2 px-4 inline-block">{message?.text}</p>
                                    </div>
                                )}
                            </>
                        ))}
                        {isLoading && (
                            <div className="">Loading...</div>
                        )}
                    </div>


                    <form className="p-4 border-t flex" onSubmit={handleMessageSubmit} >
                        {/* prompt type can be used to define the chatbot user type */}
                        {/* <select
                                value={promptType}
                                onChange={handlePromptTypeChange}
                                className=""
                            >
                                <option value="Question">Question</option>
                                <option value="Instruction">Instruction</option>
                            </select> */}
                        <input
                            type="text"
                            name="message"
                            placeholder="Type a message..."
                            className="w-full px-3 py-2 border rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                        <button type="submit" id="send-button" className="bg-silas-dark text-white px-4 py-2 rounded-r-md hover:bg-silas-medium transition duration-300">Send</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default ChatBot;